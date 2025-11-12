import streamlit as st
from definitons import Reader, QA
st.title("Mutlimodal Data  Processing System")
uploaded_file=st.file_uploader("upload your file",['pdf','docx','txt','md','pptx','png','jpg','mp3','mp4','youtube'])
reader=Reader()

def main():
    text=None
    if uploaded_file:
        if uploaded_file.name.endswith('pdf'):
            text=reader.pdf_reader(uploaded_file)
        elif uploaded_file.name.endswith('docx'):
            text=reader.docx_reader(uploaded_file)     
        elif uploaded_file.name.endswith('txt') or uploaded_file.name.endswith('md'):
            text=reader.text_reader(uploaded_file)
        elif uploaded_file.name.endswith('pptx'):
            text=reader.pptx_reader(uploaded_file)
            print(text)
        elif uploaded_file.name.endswith('png') or uploaded_file.name.endswith('jpg'):
            text = reader.image_reader(uploaded_file)
            print(text)
        elif uploaded_file.name.endswith('.mp4'):
           text=reader.video_reader(uploaded_file)
        elif uploaded_file.name.endswith('.mp3'):
           text=reader.audio_reader(uploaded_file)
    
    if text:
        qa=QA(text)
        question=st.chat_input('enter your question')
        if question:
            answer=qa.QuestionAnswering(question)
            st.write("answer:",answer)
            

if __name__=='__main__':
    main()