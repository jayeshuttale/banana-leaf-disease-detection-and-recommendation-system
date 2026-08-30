import streamlit as st
import requests

st.set_page_config(page_title="Banana Leaf Disease Detection", layout="centered")
st.title("🍌 Banana Leaf Disease Detection & Recommendation")
st.caption("This tool provides general guidance and does not replace professional agricultural diagnosis.")

uploaded_file = st.file_uploader("Upload a banana leaf image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded image", use_container_width=True)

    if st.button("Analyze"):
        with st.spinner("Analyzing..."):
            files = {'image': uploaded_file.getvalue()}
            response = requests.post('http://localhost:5000/predict', files=files)

        if response.status_code == 200:
            result = response.json()

            if not result['valid']:
                st.warning(result['message'])
            else:
                st.subheader(f"Prediction: {result['class']}")
                st.metric("Confidence", f"{result['confidence']}%")

                rec = result['recommendation']
                st.subheader("Disease information")
                st.write(rec.get('disease_info', ''))

                if rec.get('symptoms'):
                    st.subheader("Symptoms")
                    for s in rec['symptoms']:
                        st.write(f"- {s}")

                st.subheader("Management")
                for m in rec.get('management', []):
                    st.write(f"- {m}")

                st.subheader("Prevention")
                for p in rec.get('prevention', []):
                    st.write(f"- {p}")
        else:
            st.error("Prediction failed. Check that the backend server is running.")