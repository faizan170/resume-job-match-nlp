data = '''
We build cutting edge Cloud based solutions which are used by over 15000 companies around the world, predominantly in the US, Australia and Canada. Our goal is to be the leading SaaS provider for enterprises by 2020. Our customers include NASA, 3M, Disney, Amazon etc.

We're looking for Deep Learning Engineers who can add value to our products through AI/ML for recommendations, pattern identifications and a 'smarter' system to improve efficiency of our solutions.

You must:
Put Machine Learning algorithms into practice
Have excellent understanding of Statistics and foundations of Deep Learning.
Have sound engineering foundations and ability to build production ready services (and not just prototypes)
Strong programming skills in an OO language
Understanding of building efficient and optimized systems to parallelize operations (eg through GPUs) for quick response times

You will be responsible for:
Building pipelines for deep learning that can handle significant data
Executing experiments for hypothesis testing
Constantly optimizing
'''
from docx import Document
from docx.shared import Inches

document = Document()

p = document.add_paragraph(data)
document.save('demo.docx')