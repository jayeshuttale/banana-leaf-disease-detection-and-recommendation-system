import streamlit as st
import requests

# Set page config to wide mode for responsive split layout
st.set_page_config(
    page_title="Banana Leaf Disease Detection & Advisory",
    page_icon="🍌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for rich aesthetics, image sizing, and responsive design
st.markdown("""
<style>
    /* Main container styling - adequate top padding so header is not cropped under Streamlit toolbar */
    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 1300px;
    }
    
    /* Header typography */
    .header-title {
        font-size: 2.2rem;
        font-weight: 700;
        line-height: 1.3;
        margin-top: 0.5rem;
        margin-bottom: 0.3rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Responsive image container */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 12px;
        padding: 8px;
        margin-bottom: 1rem;
    }
    [data-testid="stImage"] img {
        max-height: 350px !important;
        width: auto !important;
        max-width: 100% !important;
        object-fit: contain !important;
        border-radius: 8px;
    }
    
    /* Card containers */
    .custom-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 14px;
        padding: 1.25rem;
        margin-bottom: 1.2rem;
        backdrop-filter: blur(10px);
    }
    
    /* Prediction Banner Badges */
    .badge-healthy {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        color: white;
        padding: 0.8rem 1.25rem;
        border-radius: 10px;
        font-weight: 600;
        font-size: 1.15rem;
        margin-bottom: 1rem;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: center;
        gap: 0.5rem;
    }
    .badge-disease {
        background: linear-gradient(135deg, #dc2626 0%, #ea580c 100%);
        color: white;
        padding: 0.8rem 1.25rem;
        border-radius: 10px;
        font-weight: 600;
        font-size: 1.15rem;
        margin-bottom: 1rem;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: center;
        gap: 0.5rem;
    }
    .badge-warning {
        background: linear-gradient(135deg, #d97706 0%, #f59e0b 100%);
        color: white;
        padding: 0.8rem 1.25rem;
        border-radius: 10px;
        font-weight: 600;
        font-size: 1.05rem;
        margin-bottom: 1rem;
    }
    
    /* Recommendation item cards */
    .rec-item {
        background: rgba(255, 255, 255, 0.03);
        border-left: 3px solid #10b981;
        padding: 0.6rem 0.9rem;
        margin-bottom: 0.5rem;
        border-radius: 0 8px 8px 0;
        font-size: 0.95rem;
    }
    .symptom-item {
        background: rgba(239, 68, 68, 0.08);
        border-left: 3px solid #ef4444;
        padding: 0.6rem 0.9rem;
        margin-bottom: 0.5rem;
        border-radius: 0 8px 8px 0;
        font-size: 0.95rem;
    }
    .placeholder-box {
        text-align: center;
        padding: 3rem 1.5rem;
        border: 2px dashed rgba(255, 255, 255, 0.15);
        border-radius: 16px;
        color: #94a3b8;
    }
</style>
""", unsafe_allow_html=True)

# Top Application Header
st.markdown('<div class="header-title">🍌 Banana Leaf Disease Detection & Advisory</div>', unsafe_allow_html=True)
st.caption("AI-powered diagnostic tool providing real-time crop disease classification and expert management recommendations.")

# Responsive 2-Column Layout
col_left, col_right = st.columns([5, 6], gap="large")

# Initialize session state keys
if "uploader_key" not in st.session_state:
    st.session_state["uploader_key"] = 0

def reset_image_state():
    st.session_state["uploader_key"] += 1
    st.session_state.pop("last_result", None)
    st.session_state.pop("current_file_name", None)
    if hasattr(st, "rerun"):
        st.rerun()
    elif hasattr(st, "experimental_rerun"):
        st.experimental_rerun()

# ----------------- LEFT COLUMN: Upload & Preview -----------------
with col_left:
    st.markdown("### 📤 Upload & Preview")
    
    uploaded_file = st.file_uploader(
        "Choose a clear image of a banana leaf",
        type=['jpg', 'jpeg', 'png'],
        help="Upload JPG, JPEG, or PNG formats.",
        key=f"leaf_uploader_{st.session_state['uploader_key']}"
    )

    analyze_clicked = False

    if uploaded_file is not None:
        # Detect if user uploaded a different file
        if "current_file_name" in st.session_state and st.session_state["current_file_name"] != uploaded_file.name:
            st.session_state.pop("last_result", None)
        st.session_state["current_file_name"] = uploaded_file.name

        try:
            st.image(uploaded_file, caption="Selected Leaf Preview", use_column_width=True)
        except TypeError:
            st.image(uploaded_file, caption="Selected Leaf Preview")
        
        # Display buttons based on analysis state
        if "last_result" in st.session_state:
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                analyze_clicked = st.button("🔍 Re-Analyze", type="primary", use_container_width=True)
            with btn_col2:
                if st.button("🔄 New Image", use_container_width=True):
                    reset_image_state()
        else:
            analyze_clicked = st.button("🔍 Analyze Leaf Image", type="primary", use_container_width=True)
    else:
        st.info("💡 **Tip**: For best diagnosis, upload a well-lit, in-focus photo showing the leaf surface.")

# ----------------- RIGHT COLUMN: Diagnosis & Advisory -----------------
with col_right:
    st.markdown("### 🔬 Diagnosis & Recommendations")

    if uploaded_file is None:
        st.markdown("""
        <div class="placeholder-box">
            <div style="font-size: 3rem; margin-bottom: 0.75rem;">🌿</div>
            <div style="font-size: 1.2rem; font-weight: 600; color: #e2e8f0; margin-bottom: 0.5rem;">Awaiting Leaf Image</div>
            <p style="font-size: 0.9rem; margin-bottom: 0;">Upload a banana leaf photo on the left and click <b>Analyze</b> to inspect disease symptoms and treatment options.</p>
        </div>
        """, unsafe_allow_html=True)

    elif uploaded_file is not None and not analyze_clicked and "last_result" not in st.session_state:
        st.markdown("""
        <div class="placeholder-box">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">👆</div>
            <div style="font-size: 1.15rem; font-weight: 600; color: #e2e8f0; margin-bottom: 0.3rem;">Image Ready</div>
            <p style="font-size: 0.9rem; margin-bottom: 0;">Click the <b>Analyze Leaf Image</b> button on the left to start AI diagnosis.</p>
        </div>
        """, unsafe_allow_html=True)

    # Perform analysis
    if analyze_clicked:
        with st.spinner("Analyzing leaf with MobileNetV2..."):
            try:
                files = {'image': uploaded_file.getvalue()}
                response = requests.post('http://127.0.0.1:5000/predict', files=files, timeout=30)
                
                if response.status_code == 200:
                    st.session_state["last_result"] = response.json()
                else:
                    st.session_state["last_result"] = {"error": "Server error processing prediction."}
            except requests.exceptions.ConnectionError:
                st.session_state["last_result"] = {"error": "Cannot connect to Flask backend (port 5000). Please ensure backend is running."}
            except Exception as e:
                st.session_state["last_result"] = {"error": f"Request failed: {str(e)}"}

    # Display results from state
    if "last_result" in st.session_state and uploaded_file is not None:
        result = st.session_state["last_result"]

        if "error" in result:
            st.error(f"❌ {result['error']}")
        elif not result.get('valid', False):
            st.markdown(f"""
            <div class="badge-warning">
                ⚠️ Out-of-Distribution Warning
            </div>
            """, unsafe_allow_html=True)
            st.warning(result.get('message', "This doesn't look like a banana leaf. Please upload a clear photo of a banana leaf."))
        else:
            predicted_class = result['class']
            clean_class_name = predicted_class.replace('_', ' ')
            confidence = result['confidence']
            rec = result.get('recommendation', {})

            is_healthy = predicted_class.lower() == 'healthy'
            badge_class = "badge-healthy" if is_healthy else "badge-disease"
            status_icon = "✅" if is_healthy else "⚠️"

            # Diagnosis Header Banner
            st.markdown(f"""
            <div class="{badge_class}">
                <span>{status_icon} <b>{clean_class_name}</b></span>
                <span><b>{confidence}%</b> Confidence</span>
            </div>
            """, unsafe_allow_html=True)

            # Confidence Progress Indicator
            st.progress(float(confidence) / 100.0)

            # Disease Information Section
            with st.container():
                st.markdown("#### ℹ️ Disease Overview")
                st.write(rec.get('disease_info', 'No details available.'))

            # Accordion / Tabs for structured advisory
            tab1, tab2, tab3 = st.tabs(["🔍 Symptoms", "🛡️ Management & Treatment", "🌱 Prevention"])

            with tab1:
                symptoms = rec.get('symptoms', [])
                if symptoms:
                    for s in symptoms:
                        st.markdown(f'<div class="symptom-item">• {s}</div>', unsafe_allow_html=True)
                else:
                    st.success("No disease symptoms found. Plant appears healthy!")

            with tab2:
                management = rec.get('management', [])
                if management:
                    for m in management:
                        st.markdown(f'<div class="rec-item">✓ {m}</div>', unsafe_allow_html=True)
                else:
                    st.info("No specific chemical or cultural management needed.")

            with tab3:
                prevention = rec.get('prevention', [])
                if prevention:
                    for p in prevention:
                        st.markdown(f'<div class="rec-item">🛡️ {p}</div>', unsafe_allow_html=True)
                else:
                    st.info("Standard agricultural care recommended.")

        # Quick action at bottom of results to test another image
        st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
        if st.button("🔄 Test Another Banana Leaf Image", use_container_width=True):
            reset_image_state()