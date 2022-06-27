from simple_chatbot.responses import GenericRandomResponse

# 2 tags greeting and goodbye

class GreetingResponse(GenericRandomResponse):
    choices = ("Hello! As a first time member of Ello upon signing up, you will be rewarded with xxx credits to your Touch & Go e-wallet. Are you interested to know more about this? It will only take 1 minute",
               "Hello! Ello Technology ...")


class GoodbyeResponse(GenericRandomResponse):
    choices = ("See you later.",
               "Goodbye", "Bye", "Hope you have a lovely day!",
               "See ya! Have a nice day.")

class IncentiveResponse(GenericRandomResponse):
    choices = ("What makes us different and sets us apart is that we are primarily focusing on a one stop for all platform where we cover:-Chat/messaging-Social network-Fintech-Smart Machine...In summary, we aim to provide a more interconnected virtual world where digital finance meets social media. A place where your data is yours alone!",)


class CredibleResponse(GenericRandomResponse):
    choices = ("Ello currently has associations with several reputable and trustworthy organizations. Some of them include:-Nanyang Technological University-ETHZurich (Switzerland)-Cognizant (USA)-Wise (London)-Andreessen Horowitz (Silicon Valley, California)",)

class DataPrivacyResponse(GenericRandomResponse):
    choices = ("Ello prides itself in top notch consumer data privacy. What sets us apart from other currently available tools in the market is our focus on Distributed Ledger Technology (DLT) at every stage of data collection and transmission.\nThis essentially means that your data is yours alone. Do let me know if you would like me to elaborate on the technicalities of how your data is stored.",)

class TechQResponse(GenericRandomResponse):
    choices = ("In layman terms, your data is broken into bits and stored across several databases. No central authority or intermediary, including ello has access to your data.",)

class ChatQResponse(GenericRandomResponse):
    choices = ("It’s a space where you can safely share your thoughts, feelings, beliefs, experiences, memories, dreams – your “private perceptual world.” No longer fear data leaks or your conversations being viewed by prying eyes with the help of our decentralized blockchain platform.",)

class SocialQResponse(GenericRandomResponse):
    choices = ("No longer fear your likes and interests being profiled. No longer experience targeted ads based on your like history and conversations.",)


class SmartMachineQResponse(GenericRandomResponse):
    choices = ("Our smart machine system features an AI bot which will learn about you from your patterns on the ello platform. It is essentially a personalized virtual assistant that will help you navigate your daily life.",)


class FintechProductResponse(GenericRandomResponse):
    choices = ("We offer a range of financial solutions on the ello digital space called ellopay, ellogem, exello and wello. Ellopay is an e-pay service, wello is our e-wallet tailored to the ello ecosystem, ellogem and exello are ... investment products.",)

class ReturnStrategyResponse(GenericRandomResponse):
    choices = ("We are currently performing above the market at x% per annum. Our strategy focuses on a global mindset, targeted niche market investment and long-term sustainability.\n\nWith a global perspective we are able to enter major markets around the world for the best possible returns and opportunities.\n\nIdentifying targeted niche markets that may offer long-term value allows us to steer away from competitors and maximize our gains.\n\nA long-term approach allows us to maintain steady returns.\n\nWe are able to cater to a range of client demographics, with tailored strategies depending on their financial goals. Data from usage of the ello platform, further helps us to utilize data science strategies to generate financial solutions to optimize your chances of gaining higher returns.",)


class InterestCheckResponse(GenericRandomResponse):
    choices = ("Are you interested in knowing more?",)

class LegalResponse(GenericRandomResponse):
    choices = ("Ello has been approved by the following financial bodies:\n\n    -Bank Negara Malaysia\n\n    -Ministry of Finance, Malaysia\n\nPlease find ello on the BNM list of Non-Bank E-Money Issuers:\n\nhttps://www.bnm.gov.my/non-bank-e-money-issuers",)

class PositiveOneResponse(GenericRandomResponse):
    choices = ("Great key in 'start' to proceed with the survey, after which you will be redirected to our invitation link.",)

class NegativeOneResponse(GenericRandomResponse):
    choices = ("Our deepest apologies for the inconvenience caused. Do reach out to us via ... should you have any other enquiries regarding Ello's services and products. Goodbye! Wishing you a lovely day from the Ello Technology.",)

class StartResponse(GenericRandomResponse):
    choices = ("Type 'start' to proceed with the survey",)

class Q1Response(GenericRandomResponse):
    choices = ("Q1: What type of Loan are you currently having right now (i.e. Property, Personal, Education, Medical, Auto, Business, None)",)

class Q1PositiveResponse(GenericRandomResponse):
    choices = ("Q2: From Scale 1 to 5 (5 being the highest), Will a well structured Loan improve you financial and social wellbeing right now?",)

class Q2PositiveResponse(GenericRandomResponse):
    chocies = ("Q3: Are you currently using any BNPL at the moment ('A' for Yes /'B' for No)",)

class Q3PositiveResponse(GenericRandomResponse):
    choices = ("Q4: What is the loan amount that you think ideally can help you reduce some of the financial commitment / burden right now? Please respond with the format 'MYR xxx'",)

class Q4PositiveResponse(GenericRandomResponse):
    choices = ("Q5: And last question; are you currently renting or owning the place that you are staying right now?",)

class Q5PositiveResponse(GenericRandomResponse):
    choices = ("Thank you very much. We really appreciate you taking your time to know more about this.\n\nHere is the Invitation Link :\n\nwww.ello.sg. \n\nThis link will be active for the next 48 hours. Enjoy your TnG e-wallet credits! We look forward to greeting you as a member of Ello.",)

class OthersResponse(GenericRandomResponse):
    choices = ("New Pattern! Needs to be added.",)
