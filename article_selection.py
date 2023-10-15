data = {
  "povs": [
    {
      "pov_title": "Inclusion of Transgender Athletes", 
      "description": "This perspective focuses on upholding the rights of transgender athletes to participate in women's sports, consistent with their gender identities. Advocates emphasize inclusivity, equality, and the idea that sport, like other societal systems, should adapt to embrace diverse identities."
    },
    {
      "pov_title": "Fairness and Safety in Women’s Sports", 
      "description": "This viewpoint draws attention to potential risks associated with allowing transgender women to compete in women's sports. The primary concerns revolve around perceived unfair physical advantages that transgender women, due to their possible physiological characteristics, may have over cisgender women, and the potential safety implications of such disparity."
    }
  ],
  "scale": [
    {
      "level_title": "Strongly Inclusive", 
      "description": "Articles that strongly advocate for the inclusion of transgender women in women's sports. They substantially focus on human rights, equality and diversity aspects, paying little regard to physical advantage concerns."
    },
    {
      "level_title": "Inclusive", 
      "description": "Articles that lean toward the inclusion of transgender women but still address some concerns about potential physical advantages or safety issues."
    },
    {
      "level_title": "Neutral / Balanced", 
      "description": "Articles that balance both points of view, giving equal importance to the rights of transgender athletes and the concerns about fairness and safety in women's sports."
    },
    {
      "level_title": "Concerned about Fairness and Safety", 
      "description": "Articles that lean toward concerns about potential physical advantages or safety issues, but still recognize the rights of transgender athletes."
    },
    {
      "level_title": "Strongly Concerned about Fairness and Safety", 
      "description": "Articles that majorly emphasis on potential physical advantages or safety issues related to the inclusion of transgender athletes in women's sports, paying little regard to inclusion and rights aspects."
    }
  ],
  "articles": [
    {
      "title": "Title IX and the New Protestng Rule on Transgender Athletes Explained", 
      "url": "https://www.nytimes.com/article/title-ix-transgender-athletes-school-sports.html", 
      "media": "The New York Times", 
      "summary": "The Biden administration proposes a new rule allowing schools to reject transgender athletes from competing on sports teams that align with their gender identity when questions of physicality and fairness arise. The rule would also prevent schools from introducing blanket bans on transgender athletes.", 
      "level": "3"
    },
    {
      "title": "Biden Plan Sets New Rules for Transgender Athletes and School Sports ...", 
      "url": "https://www.nytimes.com/2023/04/06/us/transgender-athletes-title-ix-biden-adminstration.html", 
      "media": "The New York Times", 
      "summary": "The Biden administration's proposed rule would permit schools to limit the participation of transgender students if including them could compromise competitive fairness or lead to sports-related injuries. However, schools would be prohibited from implementing across-the-board bans. The proposed rule requires a period of public comment before implementation.", 
      "level": "3"
    },
    {
      "title": "For Transgender Athletes, an Ongoing Search for Inclusion and Fairness ...", 
      "url": "https://www.nytimes.com/2022/06/22/sports/olympics/transgender-athletes-fina.html", 
      "media": "The New York Times", 
      "summary": "FINA, the world governing body for swimming, has proposed creating an open category of competition to 'protect competitive fairness', which some critics say is unfair to transgender athletes. The controversy over including transgender and intersex athletes in sports is one of the most divisive issues in sports.", 
      "level": "4"
    },
    {
      "title": "Transgender athletes - News, Research and Analysis - The Conversation ...", 
      "url": "https://theconversation.com/au/topics/transgender-athletes-37174", 
      "media": "The Conversation", 
      "summary": "A compilation of articles discusses the ongoing controversy over the participation of transgender athletes in sports. This page does not contain any new reporting but instead presents a diversity of perspectives and research on the topic.", 
      "level": "3"
    },
    {
      "title": "Transgender athletes: What do the scientists say? - BBC Sport", 
      "url": "https://www.bbc.com/sport/61346517", 
      "media": "BBC Sport", 
      "summary": "The article delves into the ongoing debate around the inclusion of transgender women in women's sports. It explores different scientific perspectives on whether the physiological attributes of trans women may confer unfair advantages and if exclusions or a separate category should be created for sports.", 
      "level": "3"
    },
    {
      "title": "Transgender Athletes Face Bans From Girls' Sports in 10 U.S. States",
      "url": "https://www.nytimes.com/article/transgender-athlete-ban.html",
      "media": "The New York Times",
      "summary": "Report discusses various bans or limitations on the participation of transgender girls and women in girls’ and women’s sports that have been enacted in nine states, most notably Texas. There is an expectation for more legislative action in the future.",
      "level": "4"
    },
    {
      "title": "Biden Administration Proposes New Rule for Transgender Athletes",
      "url": "https://www.wsj.com/articles/biden-administration-proposes-new-rules-for-transgender-athletes-303f9399",
      "media": "The Wall Street Journal",
      "summary": "The Biden administration proposes a new rule that prohibits total bans on transgender athletes in K-12 and college education, but allows for exclusions if necessary to maintain a level playing field.",
      "level": "3"
    }
  ]
}



def get_five_articles(data):
    i = 0
    medias = []
    levels = []
    selected = []
    #preliminary selection of unique (media, level) pairs
    for article in data["articles"]:
        media = article["media"]
        level = int(article["level"])
        if media not in medias or level not in levels:
            print(f"Just included: {media}: {media in medias}, {level}: {level in levels}")
            selected.append(article)
            levels.append(level) 
            medias.append(media)
        else:
            print(f"Already included: {media}: {media in medias}, {level}: {level in levels}")

    five_selections1 = []
    selected_medias1 = []
    five_selections2 = []
    selected_medias2 = []
    #for each level, include first article pair, none if nothing; no duplicate medias
    for i in range(1,6):
        # print(levels)
        if i in levels:
            position = levels.index(i)
            while (medias[position] in selected_medias1 and (position != len(levels)-1 and i in levels[position+1:])):
                position = levels[position+1:].index(i)
            
            # if (position == len(levels)-1 or i not in levels[position+1:]):
            #     five_selections1.append(None)
            #     print(f"{i} not levels")
            # else:
            five_selections1.append(selected[position])
            selected_medias1.append(selected[position]['media'])
            print(f"Included media {selected[position]['media']} for level {selected[position]['level']}")

        else:
            five_selections1.append(None)
            print(f"{i} not levels")

    for i in range(5, 0, -1):
        if i in levels:
            position = levels.index(i)
            while (
                selected[position]["media"] in selected_medias2
                and (position != len(levels) - 1 and i in levels[position + 1 :])
            ):
                position = levels[position + 1 :].index(i) + position + 1

            five_selections2.append(selected[position])
            selected_medias2.append(selected[position]["media"])
            print(f"Included media {selected[position]['media']} for level {selected[position]['level']}")
        else:
            five_selections2.append(None)
            print(f"{i} not in levels")

    print(selected_medias1)
    print(selected_medias2)

    if (len(list(set(selected_medias1))) >= len(list(set(selected_medias2)))):
        return five_selections1
    else:
        return five_selections2

# print(get_five_articles(data))