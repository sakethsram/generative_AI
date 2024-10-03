import IPython
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project='engaged-reducer-432905-c5' ,location='asia-east1')
multimodal_model=GenerativeModel("gemini-1.5-flash-002 ")#cheapest version of gemini availablr

c = [" tell me how gr8 alex perrira is in 20 words"]
r=multimodal_model.generate_content(c)
print(r)