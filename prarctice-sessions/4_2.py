import IPython
import vertexai
from vertexai.generative_models import GenerativeModel


vertexai.init(project='engaged-reducer-432905-c5' ,location='asia-east1')
m1=GenerativeModel("gemini-1.5-pro-001")
m2=GenerativeModel("gemini-1.5-flash-002 ")

p1=" what is beef bw alex perriera and adesanya?"
p2="based on izzy and alex p , who else has simliar beef "
P=[p1,p2]

r=m1.generate_content(P)
print(r)

