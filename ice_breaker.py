import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello LangChain")
    #    print(os.environ["OPENAI_API_KEY"])
    linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"

    #     information = """
    #     John Christopher Depp II (born June 9, 1963) is an American actor and musician. He is the recipient of multiple accolades, including a Golden Globe Award and a Screen Actors Guild Award, and has been nominated for three Academy Awards and two BAFTA awards.

    # Depp made his feature film debut in the horror film A Nightmare on Elm Street (1984) and appeared in Platoon (1986), before rising to prominence as a teen idol on the television series 21 Jump Street (1987–1990). In the 1990s, Depp acted mostly in independent films with auteur directors, often playing eccentric characters. These included Cry-Baby (1990), What's Eating Gilbert Grape (1993), Benny and Joon (1993), Dead Man (1995), Donnie Brasco (1997), and Fear and Loathing in Las Vegas (1998). Depp also began his longtime collaboration with the director Tim Burton, portraying the leads in the films Edward Scissorhands (1990), Ed Wood (1994), and Sleepy Hollow (1999).

    # In the 2000s, Depp became one of the most commercially successful film stars by playing Captain Jack Sparrow in the Walt Disney swashbuckler film series Pirates of the Caribbean (2003–2017). He also received acclaim for Chocolat (2000), Finding Neverland (2004) and Public Enemies (2009), and continued his commercially successful collaboration with Burton with the films Charlie and the Chocolate Factory (2005), Corpse Bride (2005), Sweeney Todd: The Demon Barber of Fleet Street (2007), and Alice in Wonderland (2010).

    # In 2012, Depp was one of the world's biggest film stars,[1][2] and was listed by the Guinness World Records as the world's highest-paid actor, with earnings of US$75 million in a year.[3] During the 2010s, Depp began producing films through his company Infinitum Nihil. He also received acclaim for Black Mass (2015) and formed the rock supergroup Hollywood Vampires with Alice Cooper and Joe Perry, before starring as Gellert Grindelwald in the Wizarding World films Fantastic Beasts and Where to Find Them (2016) and Fantastic Beasts: The Crimes of Grindelwald (2018).

    # Between 1998 and 2012, Depp was in a relationship with the French singer Vanessa Paradis, with whom he had two children, including the actress Lily-Rose Depp. From 2015 to 2017, Depp was married to the actress Amber Heard. Their divorce drew media attention, as both alleged abuse against each other and both engaged in highly publicized defamation cases.d8    """

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)

    print(chain.run(information=linkedin_data))

    # print(linkedin_data)
