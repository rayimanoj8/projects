import os
import openai
#
# openai.api_key = "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"
#
# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="write a love letter to my girlfriend anupama",
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
response={
  "id": "cmpl-7VlkZZEh5GRSkBDnzyUwER36cZXGg",
  "object": "text_completion",
  "created": 1687806075,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nMy dearest Anupama,\n\nWhere do I begin? How do I express the depth of my love for you?\n\nMy dear, you are so special to me. Every time I look into your eyes, I'm filled with so much joy and happiness that I never thought possible.\n\nYour presence alone comforts me, while your loving touch sends my heart into a state of euphoria. I am so blessed to call you my girlfriend. You have changed my life in ways I never imagined.\n\nYour passion and enthusiasm for life are contagious and your resilience and drive to succeed inspire me each and every day. You are the most amazing person I know and I love you with all my heart.\n\nYou make me feel safe and secure and seeing you happy always brings a smile to my face. I love having you in my life and the joy you bring to each and every moment.\n\nI hope to continue to make beautiful memories with you for years to come, and I can't wait to share my life with you.\n\nAll my love,\n\nYour boyfriend",
      "index": 0,
      "logprobs": None,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 226,
    "total_tokens": 236
  }
}
print(response["choices"][0]["text"])