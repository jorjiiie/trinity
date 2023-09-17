## Inspiration

We were inspired by simulations of human behavior by various creators such as Primer and Sethbling. Recent advances in natural language processing and large language models have enabled human-like behavior through natural language. A recent paper by Stanford researchers byPark et al [1] showcased a virtual community of generative agents that interact and communicate with each other, simulating daily activities and continuously updating the individual agent's understanding of the world. 

Following the Interactive Media track of HackMIT, we aimed to create a reality show in the VR world, allowing users to interact directly with the inhabitants of the matrix. Through continuous interaction between characters, both AI and users, the world lives and breathes on its own. 

With one catch. Through donations, viewers can cast their own influence on this tiny town. Want some drama, perhaps a love story? The fate of the characters are in your hands. 

## How we built it

We built our backend with Python using Langchain (GPT-3.5 Turbo) to simulate the agents, NLTK for sentiment analysis, while our front end is built in Unity for VR support. We also use ElevenLabs for Text-To-Speech support. 

## Challenges we ran into

The majority of our team members had never used VR or LangChain before, and figuring out the new technology with the tight deadlines was stressful but rewarding. With a lack of non-sugary drinks, we pushed through the midnight slump of pulling the project together, only to encounter many issues of version control and Git. Unity also gave us problems, with text bubbles not updating or rendering with seemingly no rhyme or reason. 

Testing our code in the VR environment was also difficult. Characters currently move randomly within the world, and getting them to walk close enough to each other to have a conversation is difficult. We ended up implementing some extra commands in Unity, which allows the person with the VR headset to grab the blob inhabitants of the town and force them to have a conversation. 

## Accomplishments that we're proud of

Though most of the logic of our project and its components are relatively simple, we’re proud that we were able to pull together so many facets of technology to build something innovative and creative. We leverage GPT for summary and for conversation, NLTK for sentiment analysis of the conversation, which offloads the amount of work delegated to GPT. We use Python for the data processing and logic of our interactions, and use Unity and ElevenLabs to breathe life into our character blobs. 
## What we learned

Beyond the technologies and frameworks, we learned how to collaborate more efficiently in Git: pushing smaller blocks more frequently to avoid merge conflicts, and continuous communication to ensure that we are working on separate, non overlapping tickets. We asked for help frequently, and delegated tasks that we did not have the brainpower to do. 

Working with LLMs, we also learned that GPT responses are, most of the time, extremely positive in their language and behavior. This meant that prompt engineering was a significant challenge. How do we write the prompts to specify a specific personality for the blobs, even if those are negative and not “GPT-like” at times? Our computation for a character’s reaction makes use of a combination of sentiment analysis and gaussian distribution to tweak the specific frequencies of reaction. We found that we had to manually reweight the positive and negative sentiments for the sentiment, and hence reactions, to be accurate. 

## What's next for Trinity

As of now, we have AI blob characters that have predefined personalities and a probability distribution detailing the probability of any reaction that they give. This means that a lot of our character’s reactions and behavior are somewhat static. Figuring out how to make dynamic reactions and potential global character developments would further enhance the believability of our reality show. 

The next big step for Trinity would be simulating a larger community of little agents, all of which you can observe and interact with. To achieve that, we would incorporate better prompt engineering for more accurate simulation of a variety of personality types, write preliminary life stories to set up a “stage” for the town we are building, incorporate databases into our system to better manage and query the information we have on the characters and their conversations, and develop more advanced VR graphics that animate our blobs with body language and emotion. 
