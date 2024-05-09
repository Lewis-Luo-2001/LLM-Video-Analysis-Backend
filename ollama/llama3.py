from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

class MyOutputParser(StrOutputParser):
    def parse(self, text):
        return text.replace('Assistant:', '')

output_parser = MyOutputParser()

llm = Ollama(model='llama3')
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a teaching assistant, I will give you subtitles of a video. Please summary the information in the video and write a paragraph, and also list the key points of the video."),
    ("user", "{input}"),
])

chain = prompt | llm | output_parser
print(chain.invoke({"input": """What would make you happy?
Can you imagine a milestone, a win, or even a material possession that would unlock
this feeling?
In this animated version of David Stindelhass, popular TED talk, brother David explains how
a simpler adjustment and how you move through the world might just change what you see,
how you feel, and how you act.
Now, my topic is greatfulness, what is the connection between happiness and greatfulness?
Many people would say, wow, that's very easy, when you're happy, you're great soul.
But think again, is it really the happy people that are great soul?
We all know quite a number of people who have everything that it would take to be happy,
and they are not happy, because they want something else, so they want more of the same.
And we all know people who have lots of misfortune, misfortune that we ourselves would not want
to have, and they are deeply happy.
The radiate happiness, they are surprised, why, because they are great soul.
Now, we can ask what really do we mean by greatfulness, and how does it work?
Something's given to us, that's valuable to us.
And it's really given, these two things have to come together, it has to be something valuable,
and it's a real gift.
And when these two things come together, then greatfulness spontaneously rises in my heart,
happiness spontaneously rises in my heart, that's how greatfulness happens.
Now, the key to all this is that we cannot only experience this once in a while.
We can be people who live greatfully, and how it can be live greatfully,
by experiencing, by becoming aware, that every moment is a given moment, as we say.
It's a gift, you have no way of assuring that there will be another moment given to you.
And yet, that's the most valuable thing that can ever be given to us.
This moment with all the opportunity that it contains.
Does that mean that we can be grateful for everything?
Certainly not.
We cannot be grateful for violence, for war, for oppression, for exploitation.
On the personal level, we cannot be grateful for the loss of the friend, for unfaithfulness,
for bereavement.
But I didn't see we can be grateful for everything, I said we can be grateful in every given moment.
For the opportunity, and even when we are confronted with something that is terribly difficult,
we can rise to this occasion and respond to the opportunity that is given to us.
So, how can each one of us find a method for living greatfully, not just once in a while being grateful,
but moment by moment to be grateful, how can we do it?
It's a very simple method.
Stop, look, go, that's all.
But how often do we stop?
We rush through life, we don't stop.
We miss the opportunity because we don't stop.
We have to stop, we have to get quiet, and we have to build stop signs into our lives.
And when you stop, then the next thing is to look.
You look, you open your eyes, you open your ears, you open your nose, you open all your senses.
For this wonderful richness that is given to us, there is no end to it.
That is what life is all about, to enjoy, to enjoy what is given to us.
But then we can also open our hearts, our hearts for the opportunity.
For the opportunity is also to help others.
To make others happy because nothing makes us more happy than when all of us are.
And when we open our hearts to the opportunities, the opportunities invite us to do something.
And that is the third stop, look, and then go and really do something.
And what we can do is whatever life offers to you in that present moment.
There is a wave of gratefulness because people are becoming aware how important this is on how this can change our world.
Because if you are grateful, you are not fearful.
If you are not fearful, you are not violent.
If you are grateful, you act out of a sense of enormous, another of a sense of scarcity, and you are willing to share.
If you are grateful, you are enjoying the differences between people, that you are respectful to everybody.
And that changes this power pyramid under which we live.
What we need is a networking of smaller groups, smaller groups who know one another, who interact with one another, and that is a grateful world.
Experiencing gratitude is closely tied to our ability to express generosity, a trait at the heart of what it means to be human.
Explore the potential of small acts of generosity to ripple out and change the world with Chris Anderson's book, Infectious Generosity.
Grab a copy here!
"""}))