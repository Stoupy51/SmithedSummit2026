to build:
- uv run stewbeet
- or `D:\advanced_desktop\SmithedSummit2026\panel> uv run --with ../../beet stewbeet` for more performance

Below is the plan for the panel on "How to Boost your Productivity" related to datapacks, presented in the 2026 Summit.
Presentation time about 35 minutes.

The people who are going to listen to this panel are beginners to experts in Minecraft datapacks.
They are familiar with the basics of datapacks, so don't need to explain everything.

Things I want to do:
- Have a pointer (using bookshelf raycast) so people can see where i'm pointing on the screen.
- Ability to launch tomatoes that explodes in red particles (redstone block) when encounter a block (check how grenades are thrown in D:\advanced_desktop\StoupGun\src)

My initial plan is:

- Introduction
- Table of Contents
- Who am I?
  - 23 years old, Data Scientist IRL
  - 7 years of datapacks (1.15), doing command blocks since they were added 13 years ago: I was 10 years old.
  - Very active developer (3000+ commits a year on GitHub), show image.
  - How I can keep up with updates and projects while having a full time job?
- 1. Explore other projects code:
  - This is the best way to discover tricks and tips other people have used that you couldn't find out on your own.
  - Read the code of experienced developers (Myriad, Gamemode 4, Bookshelf, etc.)
    - They are public on GitHub, so you can see their code.
  - Be familiar with code reading is very important, particularly for beginners and for the very next tip.
- 2. Reuse code:
  - Libraries are a great way to reuse code.
  - Don't be afraid to use libraries, they are often well thought out, optimized and tested.
  - Using abstractions is one of the best ways to boost productivity.
  - EXAMPLE, Libraries are very very important in productivity.
  - You can reuse code that are not in libraries, that's why exploring and understanding other people's code is important.
  - When you think about a system, maybe someone else has already done it, try to find it! (<= be cautious, you don't want to loose time not finding something, but you also don't want to spend time on something that is already done. With experience, you'll probably be able to tell) <= I highly recommend you to enable notifications in #resources and #projects on Minecraft Commands discord server. There are not that many messages per week so you won't be overwhelmed. https://discord.gg/QAFXFtZ
- 3. Structure your code:
  - Structure your code in a way that is easy to read and understand.
  - Use comments to explain what you are doing.
  - Make names self-explanatory.
  - Make your code modular, so that it is easy to reuse.
  - Show an example of a good structure
  - Why all of that? Because "Developers spend between 58% and 70% of their time reading source code."
    | Activity                                               | Typical Share of Time |
    | ------------------------------------------------------ | --------------------: |
    | Reading / understanding code                           |            **58–70%** |
    | Writing new code                                       |            **10–20%** |
    | Debugging, testing, and running code                   |            **10–20%** |
    | Meetings, documentation, code reviews, and other tasks |             **0–20%** |
  - Source: Xia, X., Bao, L., Lo, D., Xing, Z., E. Hassan, A., & Li, S. (2018). Measuring program comprehension: a large-scale field study with professionals. IEEE Transactions on Software Engineering, 44(10), 951-976. https://doi.org/10.1109/TSE.2017.2734091
- 4. Datapack Pre-processors / Pre-compilers:
  - What is a datapack pre-processor?
  - Why is it important and Why so many exists? https://gist.github.com/Ellivers/db296c438f9f87bbf9c79d24f940fe03
  - Examples of what you can achieve
- 5. Abstractions (with StewBeet as example):
  - What is an abstraction? https://en.wikipedia.org/wiki/Abstraction_(computer_science)
  - The good sides: code easier to read, easier to reuse, easier to maintain (update the core and everything else will be updated automatically)
  - The bad sides: each abstraction is a new concept that 1. needs to be learned (if you didn't create it yourself) 2. needs to be understood (if you created it yourself and want people to use it)
  - Visually I ride a shopping kart (mannequin), slowly accelerating and a mannequin (steve) is just walking straight ahead => Steve is faster than me at first, but as time goes I accelerate faster and go very fast.
  - In StewBeet there are abstractions for a lot of things: items, blocks, recipes, dependencies detection, etc.
    Shows examples of them and why they are POWERFUL.
- 6. 😈 Artificial Intelligence (Generative) 😈
  - *I should give everyone tomatoes in this section so they can throw them at me if they don't like it. And I should be able to disable them anytime if people are annoying me.*
  - Types of Generative AI: Image, Text/Code, Sound.
  - In the datapack community, AI is really hated due to a multitude of reasons (which I will not enter), especially Image generation. => *Here make an interactive vote where we see live results of people hating each type of AI where 5/5 = hate, 1/5 = tolerate for each type of Gen AI.*
  - Disclaimer: "If people ask how to use AI for datapacks, it means that they are not ready or skilled enough for that", ex: https://discord.com/channels/154777837382008833/1529196966981013524/1529196970583916605
  - What makes AI good at coding? => Examples, very detailled instructions, source code to explore.
  - Therefore, I'll explain how I personally use AI for datapacks and present some examples and goes into details of advantages and disadvantages.
    - A little bit (SimplEnergy): Code auto-completion, refactoring, making documentation and code comments
    - Average (StewBeet): Big refactors, creating tests, performance improvements (not mcfunction but python: pyinstrument), updating to new versions of Minecraft (ex: I read changelogs, ask AI to update, then review the changes) <= Human always have the last word and guide what the AI should work on. I don't let AI do things I don't understand. But there was a time I asked AI to explain me the cache system of Beet: "Explain me the cache system of Beet => then I understand => then "Use the beet cache system for handling dependencies versioning in StewBeet" => then I understand and can correct what was wrong. Bad example would be: "Use a cache system for handling dependencies versioning" => that's too vague, I could have not understood parts of generated code and it may have not been optimal.
    - Vibecoding demon (MC Guns Systems): 99.9% of the lines of code are AI generated, almost all is prompts. The nightmare of almost everyone here listening to me.


