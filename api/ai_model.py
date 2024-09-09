# import uuid
#
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# import os
# from langchain_core.prompts import PromptTemplate
# from langchain.chains.question_answering import load_qa_chain
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain.document_loaders import PyPDFDirectoryLoader
# from .models import Company
# import fitz
# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")
#
#
# # def get_response(company, user_question):
# #     company_name = Company.objects.filter(name=company).first()
# #     print(company_name.name)
# #     print(company_name.pdf_file.path)
# #
# #     # Use PyMuPDF to load and read the PDF content
# #     pdf_path = company_name.pdf_file.path
# #     content = ""
# #
# #     try:
# #         with fitz.open(pdf_path) as doc:
# #             for page in doc:
# #                 content += page.get_text()
# #
# #         if not content:
# #             raise ValueError("No content extracted from the PDF.")
# #
# #         text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
# #         texts = text_splitter.split_text(content)
# #
# #         if not texts:
# #             raise ValueError("No texts available to process.")
# #
# #         ids = [f"chunk-{i}" for i in range(len(texts))]
# #         embed = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=api_key)
# #
# #         vector_store = Chroma.from_texts(texts, embed, ids=ids).as_retriever()
# #
# #         prompt_template = """
# #           Please answer the question in as much detail as possible based on the provided context.
# #           Ensure to include all relevant details. If the answer is not available in the provided context,
# #           kindly respond with "The answer is not available in the context." Please avoid providing incorrect answers.
# #         \n\n
# #           Context:\n {context}?\n
# #           Question: \n{question}\n
# #
# #           Answer:
# #         """
# #         prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
# #         model = ChatGoogleGenerativeAI(model='gemini-pro', api_key=api_key, temperature=.3)
# #         chain = load_qa_chain(model, chain_type='stuff', prompt=prompt)
# #         docs = vector_store.get_relevant_documents(user_question)
# #         responses = chain(
# #             {'input_documents': docs, "question": user_question},
# #             return_only_outputs=True
# #         )
# #         return responses['output_text']
# #
# #     except Exception as e:
# #         print(f"Error reading PDF: {e}")
# #         raise ValueError("Failed to load and process the PDF.")
# # #
# def get_response(company, user_question):
#     company_name = Company.objects.filter(name=company).first()
#     print(company_name.name)
#     print(company_name.pdf_file)
#     print(company_name.pdf_file.path)
#     loader = PyPDFDirectoryLoader(company_name.pdf_file.path)
#     data = loader.load()
#     print(f"==================={data}==============")
#     text_spritter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
#     content = "\n\n".join(str(page.page_content()) for page in data)
#     texts = text_spritter.split_text(content)
#     ids = [str(uuid.uuid4()) for _ in texts]
#
#     embed = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=api_key)
#     vector_store = Chroma.from_texts(texts, embed, ids=ids).as_retriever()
#
#     prompt_template = """
#       Please answer the question in as much detail as possible based on the provided context.
#       Ensure to include all relevant details. If the answer is not available in the provided context,
#       kindly respond with "The answer is not available in the context." Please avoid providing incorrect answers.
#     \n\n
#       Context:\n {context}?\n
#       Question: \n{question}\n
#
#       Answer:
#     """
#     prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
#     model = ChatGoogleGenerativeAI(model='gemini-pro', api_key=api_key, temperature=.3)
#     chain = load_qa_chain(model, chain_type='stuff', prompt=prompt)
#     docs = vector_store.get_relevant_documents(user_question)
#     responses = chain(
#         {'input_documents': docs, "question": user_question},
#         return_only_outputs=True
#     )
#     return responses['output_text']
