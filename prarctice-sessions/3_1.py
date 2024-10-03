import vertexai
import IPython
from vertexai.generative_models import GenerativeModel


vertexai.init(project='engaged-reducer-432905-c5' ,location='asia-east1')
m=GenerativeModel("gemini-1.5-pro-001")

a=['what is the temperature in HSR layout , banglore rn? ']
b=m.generate_content(a)
print(b)

