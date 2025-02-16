

from HakariDatabase import Database

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

if __name__ == "__main__":

    IMAGE_CHARACTERS = {}

    import os

    x = """#1 - Zero Two - DARLING in the FRANXX
    \n#2 - Rem - Re:Zero kara Hajimeru Isekai Seikatsu
    \n#3 - Megumin - Kono Subarashii Sekai ni Shukufuku wo!
    \n#4 - Mai Sakurajima - Seishun Buta Yarou
    \n#5 - Rias Gremory - High School DxD
    \n#6 - Hatsune Miku - VOCALOID
    \n#7 - Power - Chainsaw Man
    \n#8 - Saber - Fate/stay night
    \n#9 - Nezuko Kamado - Kimetsu no Yaiba
    \n#10 - Satoru Gojou - Jujutsu Kaisen
    \n#11 - Asuna - Sword Art Online
    \n#12 - Nami - One Piece
    \n#13 - Mikasa Ackerman - Attack on Titan
    \n#14 - Albedo - Overlord
    \n#15 - Miku Nakano - 5-toubun no Hanayome
    \n#16 - Makima - Chainsaw Man
    \n#17 - Hange Zoë - Attack on Titan
    \n#18 - Violet Evergarden - Violet Evergarden
    \n#19 - Shinobu Kochou - Kimetsu no Yaiba
    \n#20 - Kirby - Kirby's Dream Land
    \n#21 - Nico Robin - One Piece
    \n#22 - Emilia - Re:Zero kara Hajimeru Isekai Seikatsu
    \n#23 - Aqua - Kono Subarashii Sekai ni Shukufuku wo!
    \n#24 - Akame - Akame ga Kill!
    \n#25 - Yumeko Jabami - Kakegurui
    \n#26 - Nino Nakano - 5-toubun no Hanayome
    \n#27 - Chika Fujiwara - Kaguya-sama wa Kokurasetai
    \n#28 - 2B - NieR: Automata
    \n#29 - Kaguya Shinomiya - Kaguya-sama wa Kokurasetai
    \n#30 - Marin Kitagawa - Sono Bisque Doll wa Koi wo Suru
    \n#31 - Rin Tohsaka - Fate/stay night
    \n#32 - Monkey D. Luffy - One Piece
    \n#33 - Ram - Re:Zero kara Hajimeru Isekai Seikatsu
    \n#34 - Akeno Himejima - High School DxD
    \n#35 - Bongo Cat - Internet Cats
    \n#36 - Esdeath - Akame ga Kill!
    \n#37 - Himiko Toga - Boku no Hero Academia
    \n#38 - Kurumi Tokisaki - Date A Live
    \n#39 - Roronoa Zoro - One Piece
    \n#40 - Yor Forger - SPY×FAMILY
    \n#41 - Komi Shouko - Komi-san wa, Comyushou desu.
    \n#42 - Levi - Attack on Titan
    \n#43 - Nobara Kugisaki - Jujutsu Kaisen
    \n#44 - Hinata Hyuuga - Naruto
    \n#45 - Mitsuri Kanroji - Kimetsu no Yaiba
    \n#46 - Ai Hayasaka - Kaguya-sama wa Kokurasetai
    \n#47 - Erza Scarlet - Fairy Tail
    \n#48 - Asuka Langley Soryu - Neon Genesis Evangelion
    \n#49 - Shiro - No Game No Life
    \n#50 - Gawr Gura - hololive
    \n#51 - Rei Ayanami - Neon Genesis Evangelion
    \n#52 - Tohru - Kobayashi-san Chi no Maid Dragon
    \n#53 - Raphtalia - Tate no Yuusha no Nariagari
    \n#54 - Darkness - Kono Subarashii Sekai ni Shukufuku wo!
    \n#55 - Sinon - Sword Art Online
    \n#56 - Maki Zenin - Jujutsu Kaisen
    \n#57 - Boa Hancock - One Piece
    \n#58 - Kanna Kamui - Kobayashi-san Chi no Maid Dragon
    \n#59 - Rikka Takanashi - Chuunibyou demo Koi ga Shitai!
    \n#60 - Neferpitou - Hunter × Hunter
    \n#61 - Ochako Uraraka - Boku no Hero Academia
    \n#62 - Kurisu Makise - Steins;Gate
    \n#63 - Nyan Cat - Internet Cats
    \n#64 - Truck-kun - 🤔
    \n#65 - C.C. - Code Geass: Hangyaku no Lelouch
    \n#66 - Ryuuko Matoi - Kill la Kill
    \n#67 - Itsuki Nakano - 5-toubun no Hanayome
    \n#68 - Eren Jaeger - Attack on Titan
    \n#69 - Yuuji Itadori - Jujutsu Kaisen
    \n#70 - Chiaki Nanami - Danganronpa 2: Goodbye Despair
    \n#71 - Sukuna - Jujutsu Kaisen
    \n#72 - Killua Zoldyck - Hunter × Hunter
    \n#73 - Yotsuba Nakano - 5-toubun no Hanayome
    \n#74 - Tatsumaki - One Punch Man
    \n#75 - Lucy Heartfilia - Fairy Tail
    \n#76 - Chizuru Ichinose - Kanojo, Okarishimasu
    \n#77 - Megumi Fushiguro - Jujutsu Kaisen
    \n#78 - Nagatoro-san - Ijiranaide, Nagatoro-san
    \n#79 - Osamu Dazai - Bungou Stray Dogs
    \n#80 - Yamato - One Piece
    \n#81 - Fubuki - One Punch Man
    \n#82 - Sanji - One Piece
    \n#83 - Ai Hoshino - 【OSHI NO KO】
    \n#84 - Reze - Chainsaw Man
    \n#85 - Kyouko Hori - Hori-san to Miyamura-kun
    \n#86 - Annie Leonhart - Attack on Titan
    \n#87 - Jolyne Cujoh - JoJo's Bizarre Adventure: Stone Ocean
    \n#88 - Tanjirou Kamado - Kimetsu no Yaiba
    \n#89 - Mirko - Boku no Hero Academia
    \n#90 - Taiga Aisaka - Toradora!
    \n#91 - Kanao Tsuyuri - Kimetsu no Yaiba
    \n#92 - Shoto Todoroki - Boku no Hero Academia
    \n#93 - Touka Kirishima - Tokyo Ghoul
    \n#94 - Naruto Uzumaki - Naruto
    \n#95 - Misa Amane - Death Note
    \n#96 - Katsuki Bakugou - Boku no Hero Academia
    \n#97 - Artoria Pendragon (Alter) - Fate/stay night
    \n#98 - Tsuyu Asui - Boku no Hero Academia
    \n#99 - Shouko Nishimiya - Koe no Katachi
    \n#100 - Joker - Persona 5
    \n#101 - Misato Katsuragi - Neon Genesis Evangelion
    \n#102 - Denji - Chainsaw Man
    \n#103 - Anya Forger - SPY×FAMILY
    \n#104 - Junko Enoshima - Danganronpa: Trigger Happy Havoc
    \n#105 - Sasha Braus - Attack on Titan
    \n#106 - Lucoa - Kobayashi-san Chi no Maid Dragon
    \n#107 - Crona - Soul Eater
    \n#108 - Ichika Nakano - 5-toubun no Hanayome
    \n#109 - Kobeni Higashiyama - Chainsaw Man
    \n#110 - Rukia Kuchiki - BLEACH
    \n#111 - Yuno Gasai - Mirai Nikki
    \n#112 - Kyoko Kirigiri - Danganronpa: Trigger Happy Havoc
    \n#113 - Ai Ohto - Wonder Egg Priority
    \n#114 - Kyoujurou Rengoku - Kimetsu no Yaiba
    \n#115 - Kento Nanami - Jujutsu Kaisen
    \n#116 - Hestia - Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka
    \n#117 - Shinobu Oshino - Monogatari
    \n#118 - Ken Kaneki - Tokyo Ghoul
    \n#119 - Dio Brando - JoJo's Bizarre Adventure: Phantom Blood
    \n#120 - Venom - Marvel
    \n#121 - Momo Yaoyorozu - Boku no Hero Academia
    \n#122 - Kaori Miyazono - Shigatsu wa Kimi no Uso
    \n#123 - Usagi Tsukino - Pretty Soldier Sailor Moon
    \n#124 - Giyuu Tomioka - Kimetsu no Yaiba
    \n#125 - Yukino Yukinoshita - Yahari Ore no Seishun Love Comedy wa Machigatteiru.
    \n#126 - Echidna - Re:Zero kara Hajimeru Isekai Seikatsu
    \n#127 - Tsunade - Naruto
    \n#128 - Touji Fushiguro - Jujutsu Kaisen
    \n#129 - L - Death Note
    \n#130 - Hu Tao - Genshin Impact
    \n#131 - Yoruichi Shihōin - BLEACH
    \n#132 - BMO - Adventure Time
    \n#133 - Jeanne d'Arc - Fate/Apocrypha
    \n#134 - Ishtar - Fate/Grand Order
    \n#135 - Alice Synthesis Thirty - Sword Art Online
    \n#136 - Erina Nakiri - Shokugeki no Souma
    \n#137 - Bowsette - Super Crown
    \n#138 - Mary Saotome - Kakegurui
    \n#139 - Mori Calliope - hololive
    \n#140 - Guts - Berserk
    \n#141 - Aki Hayakawa - Chainsaw Man
    \n#142 - Asuka Langley Shikinami - Rebuild of Evangelion
    \n#143 - Inugami Korone - hololive
    \n#144 - Izuku Midoriya - Boku no Hero Academia
    \n#145 - Krista Lenz - Attack on Titan
    \n#146 - Sakura Haruno - Naruto
    \n#147 - Trollface - 🤔
    \n#148 - Jotaro Kujo - JoJo's Bizarre Adventure: Stardust Crusaders
    \n#149 - Futaba Sakura - Persona 5
    \n#150 - Himeno - Chainsaw Man
    \n#151 - Hitagi Senjougahara - Monogatari
    \n#152 - Astolfo - Fate/Apocrypha
    \n#153 - Jinx - League of Legends
    \n#154 - Inosuke Hashibira - Kimetsu no Yaiba
    \n#155 - Black Hanekawa - Monogatari
    \n#156 - Itachi Uchiha - Naruto
    \n#157 - Ann Takamaki - Persona 5
    \n#158 - Roxy Migurdia - Mushoku Tensei
    \n#159 - Suguru Getou - Jujutsu Kaisen
    \n#160 - Nanika - Hunter × Hunter
    \n#161 - Sasuke Uchiha - Naruto
    \n#162 - Amelia Watson - hololive
    \n#163 - Noelle Silva - Black Clover
    \n#164 - Jeanne d'Arc (Alter) - Fate/Grand Order
    \n#165 - Mitsuha Miyamizu - Kimi no Na wa.
    \n#166 - Rio Futaba - Seishun Buta Yarou
    \n#167 - Son Goku - Dragon Ball
    \n#168 - Jibril - No Game No Life
    \n#169 - Nejire Hadou - Boku no Hero Academia
    \n#170 - Kyouka Jirou - Boku no Hero Academia
    \n#171 - Midnight - Boku no Hero Academia
    \n#172 - Lucy (CP) - Cyberpunk: Edgerunners
    \n#173 - Nao Tomori - Charlotte
    \n#174 - Tamaki Kotatsu - Enen no Shouboutai
    \n#175 - Zenitsu Agatsuma - Kimetsu no Yaiba
    \n#176 - Kurapika - Hunter × Hunter
    \n#177 - Ichigo - DARLING in the FRANXX
    \n#178 - Kakashi Hatake - Naruto
    \n#179 - Godzilla - Godzilla
    \n#180 - Maki Oze - Enen no Shouboutai
    \n#181 - Doge - 🤔
    \n#182 - Cynthia - Pokémon Diamond/Pearl/Platinum
    \n#183 - Ganyu - Genshin Impact
    \n#184 - Portgas D. Ace - One Piece
    \n#185 - Howl - Howl's Moving Castle
    \n#186 - Raven - Teen Titans
    \n#187 - Mordred - Fate/Apocrypha
    \n#188 - Android 18 - Dragon Ball Z
    \n#189 - Eri - Boku no Hero Academia
    \n#190 - Hana Uzaki - Uzaki-chan wa Asobitai!
    \n#191 - Bulma - Dragon Ball
    \n#192 - Hitori Gotou - Bocchi the Rock!
    \n#193 - Koneko Toujou - High School DxD
    \n#194 - Orihime Inoue - BLEACH
    \n#195 - Mine - Akame ga Kill!
    \n#196 - Nene Yashiro - Jibaku Shounen Hanako-kun
    \n#197 - Houshou Marine - hololive
    \n#198 - Orochimaru - Naruto
    \n#199 - Makoto Niijima - Persona 5
    \n#200 - Marceline - Adventure Time
    \n#201 - Pieck Finger - Attack on Titan
    \n#202 - Yui Hirasawa - K-ON!
    \n#203 - No-Face - Spirited Away
    \n#204 - Mina Ashido - Boku no Hero Academia
    \n#205 - Yuuta Okkotsu - Jujutsu Kaisen
    \n#206 - Kobayashi - Kobayashi-san Chi no Maid Dragon
    \n#207 - Armin Arlert - Attack on Titan
    \n#208 - Tony Tony Chopper - One Piece
    \n#209 - Alice Nakiri - Shokugeki no Souma
    \n#210 - Eris Boreas Greyrat - Mushoku Tensei
    \n#211 - Madoka Kaname - Mahou Shoujo Madoka★Magica
    \n#212 - Raiden Shogun - Genshin Impact
    \n#213 - Phosphophyllite - Houseki no Kuni
    \n#214 - Celestia Ludenberg - Danganronpa: Trigger Happy Havoc
    \n#215 - Elma - Kobayashi-san Chi no Maid Dragon
    \n#216 - Juvia Lockser - Fairy Tail
    \n#217 - Kanae Kochou - Kimetsu no Yaiba
    \n#218 - Mirai Kuriyama - Kyoukai no Kanata
    \n#219 - Yoko Littner - Tengen Toppa Gurren Lagann
    \n#220 - Hoshimachi Suisei - hololive
    \n#221 - Aiz Wallenstein - Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka
    \n#222 - Vladilena Milizé - 86 -Eighty Six-
    \n#223 - Mashiro Shiina - Sakurasou no Pet na Kanojo
    \n#224 - Booette - Super Crown
    \n#225 - Shinoa Hiiragi - Owari no Seraph
    \n#226 - Ichigo Kurosaki - BLEACH
    \n#227 - Toge Inumaki - Jujutsu Kaisen
    \n#228 - Ymir - Attack on Titan
    \n#229 - Chitoge Kirisaki - Nisekoi
    \n#230 - Eru Chitanda - Hyouka
    \n#231 - Nero Claudius - Fate/EXTRA
    \n#232 - Mt. Lady - Boku no Hero Academia
    \n#233 - Chuuya Nakahara - Bungou Stray Dogs
    \n#234 - Senko - Sewayaki Kitsune no Senko-san
    \n#235 - Faye Valentine - Cowboy Bebop
    \n#236 - Dabi - Boku no Hero Academia
    \n#237 - A2 - NieR: Automata
    \n#238 - Schwi Dola - No Game No Life
    \n#239 - Ghostface - Scream
    \n#240 - Wiz - Kono Subarashii Sekai ni Shukufuku wo!
    \n#241 - Leon S. Kennedy - Resident Evil 2
    \n#242 - Kirari Momobami - Kakegurui
    \n#243 - Wojak - 🤔
    \n#244 - Hanako-kun - Jibaku Shounen Hanako-kun
    \n#245 - Elizabeth Liones - Nanatsu no Taizai
    \n#246 - Shirakami Fubuki - hololive
    \n#247 - Xenovia Quarta - High School DxD
    \n#248 - Joseph Joestar - JoJo's Bizarre Adventure: Battle Tendency
    \n#249 - Usada Pekora - hololive
    \n#250 - Tanya Degurechaff - Youjo Senki
    \n#251 - Sumi Sakurasawa - Kanojo, Okarishimasu
    \n#252 - Kasumi Miwa - Jujutsu Kaisen
    \n#253 - Shouyou Hinata - Haikyuu!!
    \n#254 - Ninomae Ina'nis - hololive
    \n#255 - Gon Freecss - Hunter × Hunter
    \n#256 - Mewtwo - Pokédex
    \n#257 - Sakura Matou - Fate/stay night
    \n#258 - Osana Najimi - Komi-san wa, Comyushou desu.
    \n#259 - Kagamine Rin - VOCALOID
    \n#260 - Mash Kyrielight - Fate/Grand Order
    \n#261 - Mio Akiyama - K-ON!
    \n#262 - Yoru - Chainsaw Man
    \n#263 - Nagito Komaeda - Danganronpa 2: Goodbye Despair
    \n#264 - Tengen Uzui - Kimetsu no Yaiba
    \n#265 - Shizuku Murasaki - Hunter × Hunter
    \n#266 - Ruka Sarashina - Kanojo, Okarishimasu
    \n#267 - Light Yagami - Death Note
    \n#268 - Nanachi - Made in Abyss
    \n#269 - Alluka Zoldyck - Hunter × Hunter
    \n#270 - Sung Jin-Woo - Solo Leveling
    \n#271 - Nico Yazawa - Love Live! School idol project
    \n#272 - Yunyun - Kono Subarashii Sekai ni Shukufuku wo!
    \n#273 - Nero - Black Clover
    \n#274 - Daki - Kimetsu no Yaiba
    \n#275 - Hawks - Boku no Hero Academia
    \n#276 - Elaina - Majo no Tabitabi
    \n#277 - Ibuki Mioda - Danganronpa 2: Goodbye Despair
    \n#278 - Kiryu Coco - hololive
    \n#279 - Spider-Gwen (Gwen Stacy) - Marvel
    \n#280 - Leone - Akame ga Kill!
    \n#281 - Nekomata Okayu - hololive
    \n#282 - Revy - Black Lagoon
    \n#283 - Homura Akemi - Mahou Shoujo Madoka★Magica
    \n#284 - Foo Fighters - JoJo's Bizarre Adventure: Stone Ocean
    \n#285 - Zhongli - Genshin Impact
    \n#286 - Shalltear Bloodfallen - Overlord
    \n#287 - Perona - One Piece
    \n#288 - Gunter - Adventure Time
    \n#289 - Krul Tepes - Owari no Seraph
    \n#290 - Trafalgar Law - One Piece
    \n#291 - Emma - Yakusoku no Neverland
    \n#292 - Shikimori-san - Kawaii dake ja Nai Shikimori-san
    \n#293 - Mew - Pokédex
    \n#294 - Winry Rockbell - Fullmetal Alchemist
    \n#295 - Nefertari Vivi - One Piece
    \n#296 - Xiao - Genshin Impact
    \n#297 - Cloud Strife - Final Fantasy VII
    \n#298 - Suzune Horikita - Classroom of the Elite
    \n#299 - Destiny - { tákt op. }
    \n#300 - Saitama - One Punch Man
    \n#301 - Harley Quinn (Harleen Quinzel) - DC
    \n#302 - Spider-Man (Peter Parker) - Marvel
    \n#303 - Cha Hae-In - Solo Leveling
    \n#304 - Tohka Yatogami - Date A Live
    \n#305 - Kiana Kaslana - Honkai Impact 3rd
    \n#306 - Chelsea - Akame ga Kill!
    \n#307 - Mikan Tsumiki - Danganronpa 2: Goodbye Despair
    \n#308 - Chousou - Jujutsu Kaisen
    \n#309 - Mei Misaki - Another
    \n#310 - Nazuna Nanakusa - Yofukashi no Uta
    \n#311 - Crewmate - Among Us
    \n#312 - Umaru Doma - Himouto! Umaru-chan
    \n#313 - Edward Elric - Fullmetal Alchemist
    \n#314 - Akaza - Kimetsu no Yaiba
    \n#315 - Atsuko Kagari - Little Witch Academia
    \n#316 - Yui Yuigahama - Yahari Ore no Seishun Love Comedy wa Machigatteiru.
    \n#317 - Ilulu - Kobayashi-san Chi no Maid Dragon
    \n#318 - Maka Albarn - Soul Eater
    \n#319 - Yae Miko - Genshin Impact
    \n#320 - Tobio Kageyama - Haikyuu!!
    \n#321 - Ino Yamanaka - Naruto
    \n#322 - Hisoka - Hunter × Hunter
    \n#323 - Sonic the Hedgehog - Sonic the Hedgehog
    \n#324 - Miia - Monster Musume no Iru Nichijou
    \n#325 - Ereshkigal - Fate/Grand Order
    \n#326 - Giorno Giovanna - JoJo's Bizarre Adventure: Golden Wind
    \n#327 - Leafa - Sword Art Online
    \n#328 - Ririka Momobami - Kakegurui
    \n#329 - Asa Mitaka - Chainsaw Man
    \n#330 - Mikoto Misaka - Toaru
    \n#331 - Rangiku Matsumoto - BLEACH
    \n#332 - Lelouch Lamperouge - Code Geass: Hangyaku no Lelouch
    \n#333 - Eijirou Kirishima - Boku no Hero Academia
    \n#334 - Yuuki Konno - Sword Art Online
    \n#335 - Mei Hatsume - Boku no Hero Academia
    \n#336 - Muichirou Tokitou - Kimetsu no Yaiba
    \n#337 - Miko Iino - Kaguya-sama wa Kokurasetai
    \n#338 - Kenma Kozume - Haikyuu!!
    \n#339 - Hibana - Enen no Shouboutai
    \n#340 - Ruby Hoshino - 【OSHI NO KO】
    \n#341 - Diane - Nanatsu no Taizai
    \n#342 - Toph Beifong - Avatar: The Last Airbender
    \n#343 - Usopp - One Piece
    \n#344 - Holo - Ookami to Koushinryou
    \n#345 - Nelliel Tu Odelschwanck - BLEACH
    \n#346 - Uruha Rushia - hololive
    \n#347 - Merlin - Nanatsu no Taizai
    \n#348 - Raiden Mei - Honkai Impact 3rd
    \n#349 - Saiki Kusuo - Saiki Kusuo no Ψ Nan
    \n#350 - Quanxi - Chainsaw Man
    \n#351 - Shigeo Kageyama - Mob Psycho 100
    \n#352 - Kei Shirogane - Kaguya-sama wa Kokurasetai
    \n#353 - Kaede Azusagawa - Seishun Buta Yarou
    \n#354 - Beatrice (RZ) - Re:Zero kara Hajimeru Isekai Seikatsu
    \n#355 - Starfire - Teen Titans
    \n#356 - Casca - Berserk
    \n#357 - Aigis - Persona 3
    \n#358 - Venti - Genshin Impact
    \n#359 - Megurine Luka - VOCALOID
    \n#360 - Iris - Enen no Shouboutai
    \n#361 - Kuroka - High School DxD
    \n#362 - Mikey - Tokyo卍Revengers
    \n#363 - Asia Argento - High School DxD
    \n#364 - Fushi - Fumetsu no Anata e
    \n#365 - Azusa Nakano - K-ON!
    \n#366 - Satsuki Kiryuuin - Kill la Kill
    \n#367 - Uta - One Piece Film: Red
    \n#368 - Shanks - One Piece
    \n#369 - Akiko Yosano - Bungou Stray Dogs
    \n#370 - Gudetama - Gudetama
    \n#371 - Rider - Fate/stay night
    \n#372 - Anna Nishikinomiya - Shimoneta to Iu Gainen ga Sonzai Shinai Taikutsu na Sekai
    \n#373 - Yato - Noragami
    \n#374 - Shouta Aizawa - Boku no Hero Academia
    \n#375 - Mirajane Strauss - Fairy Tail
    \n#376 - Tsukasa Yuzaki - Tonikaku Kawaii
    \n#377 - Rize Kamishiro - Tokyo Ghoul
    \n#378 - Hello Kitty - Hello Kitty
    \n#379 - Stella Vermillion - Rakudai Kishi no Cavalry
    \n#380 - Angel Devil - Chainsaw Man
    \n#381 - Konan - Naruto
    \n#382 - Asta - Black Clover
    \n#383 - Yae Sakura - Honkai Impact 3rd
    \n#384 - Sebastian Michaelis - Black Butler
    \n#385 - Tartaglia - Genshin Impact
    \n#386 - Tamayo - Kimetsu no Yaiba
    \n#387 - Haru Okumura - Persona 5
    \n#388 - Stocking Anarchy - Panty & Stocking with Garterbelt
    \n#389 - Lucy - Elfen Lied
    \n#390 - Kirito - Sword Art Online
    \n#391 - Grell Sutcliff - Black Butler
    \n#392 - Hiyori Iki - Noragami
    \n#393 - Vi - League of Legends
    \n#394 - Evangelion Unit-01 - Neon Genesis Evangelion
    \n#395 - Mei Mei - Jujutsu Kaisen
    \n#396 - Lofi Girl - Lofi Girl
    \n#397 - Kana Arima - 【OSHI NO KO】
    \n#398 - Takanashi Kiara - hololive
    \n#399 - Meme - ME!ME!ME!
    \n#400 - Mayuri Shiina - Steins;Gate
    \n#401 - Runa Yomozuki - Kakegurui
    \n#402 - Sagiri Izumi - Eromanga-sensei
    \n#403 - Kushina Uzumaki - Naruto
    \n#404 - Satella - Re:Zero kara Hajimeru Isekai Seikatsu
    \n#405 - Loid Forger - SPY×FAMILY
    \n#406 - Siesta - The Detective Is Already Dead
    \n#407 - Milim Nava - Tensei shitara Slime Datta Ken
    \n#408 - Midari Ikishima - Kakegurui
    \n#409 - Arataka Reigen - Mob Psycho 100
    \n#410 - Josuke Higashikata - JoJo's Bizarre Adventure: Diamond Is Unbreakable
    \n#411 - All Might - Boku no Hero Academia
    \n#412 - Temari - Naruto
    \n#413 - Kanade Tachibana - Angel Beats!
    \n#414 - Tsumugi Kotobuki - K-ON!
    \n#415 - Tooru Oikawa - Haikyuu!!
    \n#416 - Minato Aqua - hololive
    \n#417 - Tsubasa Hanekawa - Monogatari
    \n#418 - Ranpo Edogawa - Bungou Stray Dogs
    \n#419 - Izumi Miyamura - Hori-san to Miyamura-kun
    \n#420 - Eevee - Pokédex
    \n#421 - Riza Hawkeye - Fullmetal Alchemist
    \n#422 - Nakiri Ayame - hololive
    \n#423 - Vegeta - Dragon Ball Z
    \n#424 - Rory Mercury - GATE
    \n#425 - Pochita - Chainsaw Man
    \n#426 - Shuna - Tensei shitara Slime Datta Ken
    \n#427 - Diamond - Houseki no Kuni
    \n#428 - Obanai Igurou - Kimetsu no Yaiba
    \n#429 - Mai Zenin - Jujutsu Kaisen
    \n#430 - Sheele - Akame ga Kill!
    \n#431 - Neco-Arc - Tsukihime
    \n#432 - Illyasviel von Einzbern - Fate/stay night
    \n#433 - Yue - Arifureta Shokugyou de Sekai Saikyou
    \n#434 - Brook - One Piece
    \n#435 - Rimuru Tempest - Tensei shitara Slime Datta Ken
    \n#436 - Aang - Avatar: The Last Airbender
    \n#437 - Shadow the Hedgehog - Sonic Adventure 2
    \n#438 - Princess Peach - Super Mario Bros.
    \n#439 - Akane Kurokawa - 【OSHI NO KO】
    \n#440 - Isla - Plastic Memories
    \n#441 - Rebecca - Cyberpunk: Edgerunners
    \n#442 - Filo - Tate no Yuusha no Nariagari
    \n#443 - Azula - Avatar: The Last Airbender
    \n#444 - Kiyoko Shimizu - Haikyuu!!
    \n#445 - Envy - Fullmetal Alchemist
    \n#446 - Mitsuki Bakugou - Boku no Hero Academia
    \n#447 - Ada Wong - Resident Evil 2
    \n#448 - Aoi Asahina - Danganronpa: Trigger Happy Havoc
    \n#449 - Dawn - Pokémon Diamond/Pearl/Platinum
    \n#450 - Eto - Tokyo Ghoul
    \n#451 - Batman (Bruce Wayne) - DC
    \n#452 - Ruka Urushibara - Steins;Gate
    \n#453 - Aoi Kanzaki - Kimetsu no Yaiba
    \n#454 - Takagi-san - Karakai Jouzu no Takagi-san
    \n#455 - Wanderer - Genshin Impact
    \n#456 - Stephanie Dola - No Game No Life
    \n#457 - Irina Shidou - High School DxD
    \n#458 - Loki (Loki Laufeyson) - Marvel
    \n#459 - Mari Setagaya - Itadaki! Seieki♡
    \n#460 - Diluc - Genshin Impact
    \n#461 - GUMI - VOCALOID
    \n#462 - Origami Tobiichi - Date A Live
    \n#463 - Ban - Nanatsu no Taizai
    \n#464 - Chisato Nishikigi - Lycoris Recoil
    \n#465 - Akai Haato - hololive
    \n#466 - Korra - The Legend of Korra
    \n#467 - Yuu Nishinoya - Haikyuu!!
    \n#468 - Kohaku - Dr. STONE
    \n#469 - Eula - Genshin Impact
    \n#470 - Arceus - Pokédex
    \n#471 - Peko Pekoyama - Danganronpa 2: Goodbye Despair
    \n#472 - Tokoyami Towa - hololive
    \n#473 - Mimosa Vermillion - Black Clover
    \n#474 - Earth-chan - Gijinka Series
    \n#475 - Katara - Avatar: The Last Airbender
    \n#476 - Frieren - Sousou no Frieren
    \n#477 - Saeko Busujima - Highschool of the Dead
    \n#478 - Spider-Man (Miles Morales) - Marvel
    \n#479 - Monika - Doki Doki Literature Club!
    \n#480 - Fuyumi Todoroki - Boku no Hero Academia
    \n#481 - Vaporeon - Pokédex
    \n#482 - Ritsu Tainaka - K-ON!
    \n#483 - Nadeko Sengoku - Monogatari
    \n#484 - Bishamon - Noragami
    \n#485 - Rindou Kobayashi - Shokugeki no Souma
    \n#486 - Sylphiette - Mushoku Tensei
    \n#487 - Touko Fukawa - Danganronpa: Trigger Happy Havoc
    \n#488 - Shishiro Botan - hololive
    \n#489 - Amber - Genshin Impact
    \n#490 - Erwin Smith - Attack on Titan
    \n#491 - Shion (TenSura) - Tensei shitara Slime Datta Ken
    \n#492 - Meowy - Chainsaw Man
    \n#493 - Carrot - One Piece
    \n#494 - Caitlyn - League of Legends
    \n#495 - Senkuu Ishigami - Dr. STONE
    \n#496 - Spike Spiegel - Cowboy Bebop
    \n#497 - Camie Utsushimi - Boku no Hero Academia
    \n#498 - Madara Uchiha - Naruto
    \n#499 - Rayquaza - Pokédex
    \n#500 - Goro Akechi - Persona 5
    \n#501 - Mio Naruse - Shinmai Maou no Testament
    \n#502 - Princess Bubblegum - Adventure Time
    \n#503 - TBH Creature - 🤔
    \n#504 - Utahime Iori - Jujutsu Kaisen
    \n#505 - Dante - Devil May Cry
    \n#506 - Sabo - One Piece
    \n#507 - Kuromi - Onegai My Melody
    \n#508 - Shinji Ikari - Neon Genesis Evangelion
    \n#509 - Ray (AoD) - Angels of Death
    \n#510 - Ouro Kronii - hololive
    \n#511 - Konata Izumi - Lucky☆Star
    \n#512 - Makomo - Kimetsu no Yaiba
    \n#513 - Tomura Shigaraki - Boku no Hero Academia
    \n#514 - Natsu Dragneel - Fairy Tail
    \n#515 - Kaedehara Kazuha - Genshin Impact
    \n#516 - Kaeya - Genshin Impact
    \n#517 - Snorlax - Pokédex
    \n#518 - Denki Kaminari - Boku no Hero Academia
    \n#519 - Momo Belia Deviluke - To LOVE-Ru
    \n#520 - Lisa Lisa - JoJo's Bizarre Adventure: Battle Tendency
    \n#521 - Seele Vollerei - Honkai Impact 3rd
    \n#522 - Makio - Kimetsu no Yaiba
    \n#523 - Okita Souji - Fate/KOHA-ACE
    \n#524 - Neptune - Hyperdimension Neptunia
    \n#525 - Kosaki Onodera - Nisekoi
    \n#526 - Ash Lynx - Banana Fish
    \n#527 - Misty - Pokémon Red/Green/Blue/Yellow
    \n#528 - Serena - Pokémon X/Y
    \n#529 - Kagamine Len - VOCALOID
    \n#530 - Chihiro Ogino - Spirited Away
    \n#531 - Inori Yuzuriha - Guilty Crown
    \n#532 - Keqing - Genshin Impact
    \n#533 - Gyro Zeppeli - JoJo's Bizarre Adventure: Steel Ball Run
    \n#534 - Miko Yotsuya - Mieruko-chan
    \n#535 - Nana Osaki - Nana
    \n#536 - 707 - Mystic Messenger
    \n#537 - Zuko - Avatar: The Last Airbender
    \n#538 - Kizuna AI - Kizuna AI Inc.
    \n#539 - Haruhi Suzumiya - Suzumiya Haruhi no Yuuutsu
    \n#540 - Chrollo Lucilfer - Hunter × Hunter
    \n#541 - Rika Kawai - Wonder Egg Priority
    \n#542 - Ellie - The Last of Us Part I
    \n#543 - Rei Hino - Pretty Soldier Sailor Moon
    \n#544 - Hinatsuru - Kimetsu no Yaiba
    \n#545 - Suma - Kimetsu no Yaiba
    \n#546 - Ahri - League of Legends
    \n#547 - Jonathan Joestar - JoJo's Bizarre Adventure: Phantom Blood
    \n#548 - Tetsurou Kuroo - Haikyuu!!
    \n#549 - Vanitas - Vanitas no Carte
    \n#550 - Senpai (TS) - Tejina-senpai
    \n#551 - Tooru Honda - Fruits Basket
    \n#552 - Morgiana - Magi
    \n#553 - Ruby Rose - RWBY
    \n#554 - Kei Tsukishima - Haikyuu!!
    \n#555 - Akane Owari - Danganronpa 2: Goodbye Despair
    \n#556 - Shirahoshi - One Piece
    \n#557 - Kotori Itsuka - Date A Live
    \n#558 - Ayane Shirakawa - Overflow ~Iretara Afureru Shimai no Kimochi~
    \n#559 - Wendy Marvell - Fairy Tail
    \n#560 - Hanabi Hyuuga - Naruto
    \n#561 - Pikachu (Species) - Pokédex
    \n#562 - Tamamo no Mae - Fate/EXTRA
    \n#563 - Kamisato Ayaka - Genshin Impact
    \n#564 - Hinata Tachibana - Tokyo卍Revengers
    \n#565 - Vanessa Enoteca - Black Clover
    \n#566 - Maika Sakuranomiya - Blend S
    \n#567 - Lisa - Genshin Impact
    \n#568 - Shrek - Shrek
    \n#569 - Karma Akabane - Ansatsu Kyoushitsu
    \n#570 - Kurome - Akame ga Kill!
    \n#571 - Lain Iwakura - Serial Experiments Lain
    \n#572 - Jessie - Pokémon: Indigo League
    \n#573 - Chocola - Nekopara
    \n#574 - Alucard - Hellsing
    \n#575 - Rin Okumura - Ao no Exorcist
    \n#576 - Nana Shimura - Boku no Hero Academia
    \n#577 - Misaki Ayuzawa - Kaichou wa Maid-sama!
    \n#578 - Genos - One Punch Man
    \n#579 - Kallen Stadtfeld - Code Geass: Hangyaku no Lelouch
    \n#580 - Blair - Soul Eater
    \n#581 - Albedo (GI) - Genshin Impact
    \n#582 - Franky - One Piece
    \n#583 - Tamaki Amajiki - Boku no Hero Academia
    \n#584 - Aoi Toudou - Jujutsu Kaisen
    \n#585 - Mereoleona Vermillion - Black Clover
    \n#586 - Meiko Honma - Anohana: The Flower We Saw That Day
    \n#587 - Wise Mystical Tree - 🤔
    \n#588 - Tsunomaki Watame - hololive
    \n#589 - Haruka Tenou - Pretty Soldier Sailor Moon
    \n#590 - Tifa Lockhart - Final Fantasy VII
    \n#591 - Bon Clay - One Piece
    \n#592 - Alice Zuberg - Sword Art Online
    \n#593 - Juuzou Suzuya - Tokyo Ghoul
    \n#594 - Trish Una - JoJo's Bizarre Adventure: Golden Wind
    \n#595 - Sayu Ogiwara - Hige wo Soru. Soshite Joshikosei wo Hiro.
    \n#596 - Mahito - Jujutsu Kaisen
    \n#597 - Minato Namikaze - Naruto
    \n#598 - Vinsmoke Reiju - One Piece
    \n#599 - Yona - Akatsuki no Yona
    \n#600 - Rossweisse - High School DxD
    \n#601 - Ryuunosuke Akutagawa - Bungou Stray Dogs
    \n#602 - Sanemi Shinazugawa - Kimetsu no Yaiba
    \n#603 - Mako Mankanshoku - Kill la Kill
    \n#604 - Vanilla - Nekopara
    \n#605 - Machi Komachine - Hunter × Hunter
    \n#606 - Nanashi Mumei - hololive
    \n#607 - Ceres Fauna - hololive
    \n#608 - Tet - No Game No Life
    \n#609 - Yuki Nagato - Suzumiya Haruhi no Yuuutsu
    \n#610 - Minako Aino - Pretty Soldier Sailor Moon
    \n#611 - The Knight - Hollow Knight
    \n#612 - Koutarou Bokuto - Haikyuu!!
    \n#613 - Mona - Genshin Impact
    \n#614 - Beidou - Genshin Impact
    \n#615 - Ikumi Mito - Shokugeki no Souma
    \n#616 - Nayuta - Chainsaw Man
    \n#617 - Yoshino - Date A Live
    \n#618 - Muzan Kibutsuji - Kimetsu no Yaiba
    \n#619 - Creeper - Minecraft
    \n#620 - AE3803 - Hataraku Saibou
    \n#621 - Lala Satalin Deviluke - To LOVE-Ru
    \n#622 - Ciel Phantomhive - Black Butler
    \n#623 - Konjiki no Yami - To LOVE-Ru
    \n#624 - Akira Fudou - Devilman
    \n#625 - Sakura Miko - hololive
    \n#626 - Aki Adagaki - Masamune-kun no Revenge
    \n#627 - Gaara - Naruto
    \n#628 - Ryuk - Death Note
    \n#629 - Megumi Tadokoro - Shokugeki no Souma
    \n#630 - Shouko Ieiri - Jujutsu Kaisen
    \n#631 - Shizue Izawa - Tensei shitara Slime Datta Ken
    \n#632 - Rui Tachibana - Domestic na Kanojo
    \n#633 - Gwen - Total Drama Island
    \n#634 - Sylveon - Pokédex
    \n#635 - Shego - Kim Possible
    \n#636 - Reki Kyan - SK∞
    \n#637 - Ookami Mio - hololive
    \n#638 - Yoshikage Kira - JoJo's Bizarre Adventure: Diamond Is Unbreakable
    \n#639 - Jean - Genshin Impact
    \n#640 - Tae Takemi - Persona 5
    \n#641 - Kagome Higurashi - InuYasha
    \n#642 - Mikaela Hyakuya - Owari no Seraph
    \n#643 - Dark Magician Girl - Yu-Gi-Oh! Trading Card Game
    \n#644 - Shirogane Noel - hololive
    \n#645 - Princess of Klaxosaurs - DARLING in the FRANXX
    \n#646 - Arataki Itto - Genshin Impact
    \n#647 - Zack - Angels of Death
    \n#648 - Jean Kirstein - Attack on Titan
    \n#649 - San - Princess Mononoke
    \n#650 - Ryu Lion - Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka
    \n#651 - Johnny Joestar - JoJo's Bizarre Adventure: Steel Ball Run
    \n#652 - Tomoko Kuroki - Watashi ga Motenai no wa dō Kangaetemo Omaera ga Warui!
    \n#653 - Yui (SAO) - Sword Art Online
    \n#654 - Chi-Chi - Dragon Ball
    \n#655 - Bruno Bucciarati - JoJo's Bizarre Adventure: Golden Wind
    \n#656 - Atsushi Nakajima - Bungou Stray Dogs
    \n#657 - Leorio Paladiknight - Hunter × Hunter
    \n#658 - The Giant Rat That Makes All of the Rules - Rat Movie
    \n#659 - Genocider Syo - Danganronpa: Trigger Happy Havoc
    \n#660 - Sarada Uchiha - Boruto: Naruto Next Generations
    \n#661 - Nagisa Shiota - Ansatsu Kyoushitsu
    \n#662 - Kaworu Nagisa - Neon Genesis Evangelion
    \n#663 - Nessa - Pokémon Sword/Shield
    \n#664 - Deadpool (Wade Wilson) - Marvel
    \n#665 - Murata Himeko - Honkai Impact 3rd
    \n#666 - Noriaki Kakyoin - JoJo's Bizarre Adventure: Stardust Crusaders
    \n#667 - Natsumi - Date A Live
    \n#668 - Irina Jelavić - Ansatsu Kyoushitsu
    \n#669 - Pain - Naruto
    \n#670 - Meruccubus - Meru The Succubus
    \n#671 - Gintoki Sakata - Gintama
    \n#672 - Death the Kid - Soul Eater
    \n#673 - Oozora Subaru - hololive
    \n#674 - Celty Sturluson - Durarara!!
    \n#675 - Douma - Kimetsu no Yaiba
    \n#676 - Kafka - Honkai: Star Rail
    \n#677 - Mami Tomoe - Mahou Shoujo Madoka★Magica
    \n#678 - Sabito - Kimetsu no Yaiba
    \n#679 - Veliona - Honkai Impact 3rd
    \n#680 - Roy Mustang - Fullmetal Alchemist
    \n#681 - Maki Nishikino - Love Live! School idol project
    \n#682 - Spider Demon (Mother) - Kimetsu no Yaiba
    \n#683 - Inuyasha - InuYasha
    \n#684 - Yoriichi Tsugikuni - Kimetsu no Yaiba
    \n#685 - Gilgamesh - Fate/stay night
    \n#686 - Yumemi Yumemite - Kakegurui
    \n#687 - Sayaka Maizono - Danganronpa: Trigger Happy Havoc
    \n#688 - Quinella - Sword Art Online
    \n#689 - Hitoshi Shinsou - Boku no Hero Academia
    \n#690 - Kokoro - DARLING in the FRANXX
    \n#691 - Kim Dokja - Omniscient Reader's Viewpoint
    \n#692 - Rin - Shelter
    \n#693 - Sonia Nevermind - Danganronpa 2: Goodbye Despair
    \n#694 - Tomoe Koga - Seishun Buta Yarou
    \n#695 - KAITO - VOCALOID
    \n#696 - 9S - NieR: Automata
    \n#697 - Koushi Sugawara - Haikyuu!!
    \n#698 - Izuna Hatsuse - No Game No Life
    \n#699 - Silica - Sword Art Online
    \n#700 - Ghislaine Dedoldia - Mushoku Tensei
    \n#701 - Ayame Kajou - Shimoneta to Iu Gainen ga Sonzai Shinai Taikutsu na Sekai
    \n#702 - Sephiroth - Final Fantasy VII
    \n#703 - Ami Mizuno - Pretty Soldier Sailor Moon
    \n#704 - Griffith - Berserk
    \n#705 - Aether - Genshin Impact
    \n#706 - Alphonse Elric - Fullmetal Alchemist
    \n#707 - My Melody - Onegai My Melody
    \n#708 - Bronya Zaychik - Honkai Impact 3rd
    \n#709 - N - Pokémon Black/White
    \n#710 - Satanichia McDowell Kurumizawa - Gabriel DropOut
    \n#711 - Lady Nagant - Boku no Hero Academia
    \n#712 - Kurenai Yuuhi - Naruto
    \n#713 - Legosi - BEASTARS
    \n#714 - Koro-sensei - Ansatsu Kyoushitsu
    \n#715 - Pepe - 🤔
    \n#716 - Rebecca (OP) - One Piece
    \n#717 - Mami Nanami - Kanojo, Okarishimasu
    \n#718 - Kaho Hinata - Blend S
    \n#719 - Tier Harribel - BLEACH
    \n#720 - Mavis Vermillion - Fairy Tail
    \n#721 - Narberal Gamma - Overlord
    \n#722 - Natsuki - Doki Doki Literature Club!
    \n#723 - Abigail Jones - Great Pretender
    \n#724 - Mavis Dracula - Hotel Transylvania
    \n#725 - Langa Hasegawa - SK∞
    \n#726 - Le Monke - 🤔
    \n#727 - William Afton - Five Nights at Freddy's 2
    \n#728 - Levy McGarden - Fairy Tail
    \n#729 - Draken - Tokyo卍Revengers
    \n#730 - Totoro - My Neighbor Totoro
    \n#731 - Mei Terumi - Naruto
    \n#732 - Yuri - Doki Doki Literature Club!
    \n#733 - Ray - Yakusoku no Neverland
    \n#734 - Adult Neptune - Megadimension Neptunia VII
    \n#735 - Son Gohan - Dragon Ball Z
    \n#736 - Alastor - Hazbin Hotel
    \n#737 - Giratina - Pokédex
    \n#738 - Rin Nohara - Naruto
    \n#739 - Yui - Angel Beats!
    \n#740 - Lumine - Genshin Impact
    \n#741 - SCP-049 - SCP Foundation
    \n#742 - Amy Rose - Sonic CD
    \n#743 - Yelan - Genshin Impact
    \n#744 - Artoria Pendragon (Lancer) - Fate/Grand Order
    \n#745 - Collei - Genshin Impact
    \n#746 - Iroha Isshiki - Yahari Ore no Seishun Love Comedy wa Machigatteiru.
    \n#747 - Jahy - Jahy-sama wa Kujikenai!
    \n#748 - Kyouka Izumi - Bungou Stray Dogs
    \n#749 - Ryou Yamada - Bocchi the Rock!
    \n#750 - Shouya Ishida - Koe no Katachi
    \n#751 - Erza Knightwalker - Fairy Tail
    \n#752 - Shylily - Independent Virtual YouTubers
    \n#753 - Videl - Dragon Ball Z
    \n#754 - Naoto Shirogane - Persona 4
    \n#755 - Yoimiya - Genshin Impact
    \n#756 - Fischl - Genshin Impact
    \n#757 - Blackfire - Teen Titans
    \n#758 - Evangelion Unit-02 - Neon Genesis Evangelion
    \n#759 - Toyomi Fujiwara - Kaguya-sama wa Kokurasetai
    \n#760 - Kei Karuizawa - Classroom of the Elite
    \n#761 - Hua Cheng - Tian Guan Ci Fu
    \n#762 - May - Pokémon Ruby/Sapphire/Emerald
    \n#763 - Mario - Super Mario Bros.
    \n#764 - Lola Bunny - Looney Tunes
    \n#765 - Chifuyu Matsuno - Tokyo卍Revengers
    \n#766 - Ironmouse - VShojo
    \n#767 - Ditto - Pokédex
    \n#768 - Yukana Yame - Hajimete no Gal
    \n#769 - Durandal - Honkai Impact 3rd
    \n#770 - Kokushibou - Kimetsu no Yaiba
    \n#771 - Keiji Akaashi - Haikyuu!!
    \n#772 - Rei Miyamoto - Highschool of the Dead
    \n#773 - Elaine - Nanatsu no Taizai
    \n#774 - Sword Maiden - Goblin Slayer
    \n#775 - Biscuit Krueger - Hunter × Hunter
    \n#776 - Kagura - Gintama
    \n#777 - Tsukasa Yugi - Jibaku Shounen Hanako-kun
    \n#778 - Mamako Oosuki - Tsujou Kogeki ga Zentai Kogeki de Ni-kai Kogeki no Okaa-san wa Suki Desuka?
    \n#779 - Suzuha Amane - Steins;Gate
    \n#780 - Kureiji Ollie - hololive
    \n#781 - Pikachu - Pokémon: Indigo League
    \n#782 - Fumino Furuhashi - Bokutachi wa Benkyou ga Dekinai
    \n#783 - Lust - Fullmetal Alchemist
    \n#784 - Ado - Utaite
    \n#785 - Yuki Tsukumo - Jujutsu Kaisen
    \n#786 - Meliodas - Nanatsu no Taizai
    \n#787 - Yami Yugi - Yu-Gi-Oh! Duel Monsters
    \n#788 - D.Va - Overwatch
    \n#789 - Mirio Togata - Boku no Hero Academia
    \n#790 - Adrien Agreste - Miraculous: Tales of Ladybug & Cat Noir
    \n#791 - Atsumu Miya - Haikyuu!!
    \n#792 - Gigachad - 🤔
    \n#793 - Tooru Hagakure - Boku no Hero Academia
    \n#794 - Caesar A. Zeppeli - JoJo's Bizarre Adventure: Battle Tendency
    \n#795 - Yukihana Lamy - hololive
    \n#796 - Derieri - Nanatsu no Taizai
    \n#797 - Enkidu - Fate/strange Fake
    \n#798 - Frederica Baumann - Re:Zero kara Hajimeru Isekai Seikatsu
    \n#799 - Michiru Kagemori - BNA: Brand New Animal
    \n#800 - Carnage - Marvel
    \n#801 - Senju Kawaragi - Tokyo卍Revengers
    \n#802 - Arcueid Brunestud - Tsukihime
    \n#803 - Freya - Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka
    \n#804 - Airi Sakura - Classroom of the Elite
    \n#805 - Star Platinum - JoJo's Bizarre Adventure: Stardust Crusaders
    \n#806 - Hina Amano - Tenki no Ko
    \n#807 - Menhera-chan - Menhera Shoujo Kurumi-chan
    \n#808 - Isuzu Sento - Amagi Brilliant Park
    \n#809 - Delta - Kage no Jitsuryokusha ni Naritakute!
    \n#810 - Ponyo - Ponyo
    \n#811 - Bayonetta - Bayonetta
    \n#812 - Ami Kawashima - Toradora!
    \n#813 - Gyoumei Himejima - Kimetsu no Yaiba
    \n#814 - Scarlet Witch (Wanda Maximoff) - Marvel
    \n#815 - Yuna (SAO) - Sword Art Online
    \n#816 - Tenten - Naruto
    \n#817 - Lugia - Pokédex
    \n#818 - Sayori - Doki Doki Literature Club!
    \n#819 - Tashigi - One Piece
    \n#820 - Yami Sukehiro - Black Clover
    \n#821 - Mimikyu - Pokédex
    \n#822 - Yoichi Isagi - Blue Lock
    \n#823 - Komi Shuuko - Komi-san wa, Comyushou desu.
    \n#824 - Aerith Gainsborough - Final Fantasy VII
    \n#825 - Ahsoka Tano - Star Wars: The Clone Wars
    \n#826 - Grumpy Cat - Internet Cats
    \n#827 - Aoi Akane - Jibaku Shounen Hanako-kun
    \n#828 - Panty Anarchy - Panty & Stocking with Garterbelt
    \n#829 - Sangonomiya Kokomi - Genshin Impact
    \n#830 - Amelie Azazel - Mairimashita! Iruma-kun
    \n#831 - Sans - UNDERTALE
    \n#832 - Jeanne - Vanitas no Carte
    \n#833 - Sophie Hatter - Howl's Moving Castle
    \n#834 - Obito Uchiha - Naruto
    \n#835 - Rise Kujikawa - Persona 4
    \n#836 - Soi Fon - BLEACH
    \n#837 - Ryuji Sakamoto - Persona 5
    \n#838 - Hakos Baelz - hololive
    \n#839 - Cinnabar - Houseki no Kuni
    \n#840 - Rock Lee - Naruto
    \n#841 - Ash Ketchum - Pokémon: Indigo League
    \n#842 - Amane Kanata - hololive
    \n#843 - Yuzuki Choco - hololive
    \n#844 - Fu Hua - Honkai Impact 3rd
    \n#845 - Yuno - Black Clover
    \n#846 - Finn - Adventure Time
    \n#847 - Ougi Oshino - Monogatari
    \n#848 - Reiner Braun - Attack on Titan
    \n#849 - Shiki Ryougi - Kara no Kyoukai: The Garden of Sinners
    \n#850 - Gray Fullbuster - Fairy Tail
    \n#851 - Itachi's Crow - Naruto
    \n#852 - Shura Kirigakure - Ao no Exorcist
    \n#853 - Feitan Portor - Hunter × Hunter
    \n#854 - Hotaru Shidare - Dagashi Kashi
    \n#855 - Guido Mista - JoJo's Bizarre Adventure: Golden Wind
    \n#856 - Megumi Katou - Saenai Heroine no Sodatekata
    \n#857 - Ramona Flowers - Scott Pilgrim
    \n#858 - GIR - Invader Zim
    \n#859 - Thorfinn - Vinland Saga
    \n#860 - Star Butterfly - Star vs. the Forces of Evil
    \n#861 - Oda Nobunaga - Fate/KOHA-ACE
    \n#862 - Jiraiya - Naruto
    \n#863 - Kyaru - Princess Connect! Re:Dive
    \n#864 - Serafall Leviathan - High School DxD
    \n#865 - Akari Watanabe - Fuufu Ijou, Koibito Miman.
    \n#866 - Shikamaru Nara - Naruto
    \n#867 - Reimu Hakurei - Touhou Koumakyou ~ the Embodiment of Scarlet Devil
    \n#868 - Charmander - Pokédex
    \n#869 - Sakura Kinomoto - Cardcaptor Sakura
    \n#870 - Mizuki Akiyama - Project SEKAI: Colorful Stage!
    \n#871 - Rikka Takarada - SSSS.GRIDMAN
    \n#872 - Shenhe - Genshin Impact
    \n#873 - Amity Blight - The Owl House
    \n#874 - Freddy Fazbear - Five Nights at Freddy's 1
    \n#875 - Phoenix Wright - Phoenix Wright: Ace Attorney
    \n#876 - Ikuyo Kita - Bocchi the Rock!
    \n#877 - High Elf Archer - Goblin Slayer
    \n#878 - Seishirou Tsugumi - Nisekoi
    \n#879 - Klee - Genshin Impact
    \n#880 - Sanic - 🤔
    \n#881 - Sakuya Izayoi - Touhou Koumakyou ~ the Embodiment of Scarlet Devil
    \n#882 - Elsa - Frozen
    \n#883 - Rohan Kishibe - JoJo's Bizarre Adventure: Diamond Is Unbreakable
    \n#884 - Kyuusaku Yumeno - Bungou Stray Dogs
    \n#885 - Gabi Braun - Attack on Titan
    \n#886 - Miko - No Game No Life
    \n#887 - Sistine Fibel - Rokudenashi Majutsu Koushi to Akashic Records
    \n#888 - Inverse Tohka - Date A Live
    \n#889 - Omaru Polka - hololive
    \n#890 - Genya Shinazugawa - Kimetsu no Yaiba
    \n#891 - Keisuke Baji - Tokyo卍Revengers
    \n#892 - Ms. Joke - Boku no Hero Academia
    \n#893 - Hajime Hinata - Danganronpa 2: Goodbye Despair
    \n#894 - Karen Araragi - Monogatari
    \n#895 - Flame Princess - Adventure Time
    \n#896 - SpongeBob SquarePants - SpongeBob SquarePants
    \n#897 - Shouko Makinohara - Seishun Buta Yarou
    \n#898 - Makoto Naegi - Danganronpa: Trigger Happy Havoc
    \n#899 - Kasumi Yoshizawa - Persona 5
    \n#900 - Mafuyu Kirisu - Bokutachi wa Benkyou ga Dekinai
    \n#901 - Soul Eater Evans - Soul Eater
    \n#902 - Fiona Frost - SPY×FAMILY
    \n#903 - 2D - Gorillaz
    \n#904 - Ningguang - Genshin Impact
    \n#905 - Illumi Zoldyck - Hunter × Hunter
    \n#906 - Bread - I Am Bread
    \n#907 - Umbreon - Pokédex
    \n#908 - Tomoe - Kamisama Hajimemashita
    \n#909 - Mai - Avatar: The Last Airbender
    \n#910 - Mayoi Hachikuji - Monogatari
    \n#911 - Coraline Jones - Coraline
    \n#912 - Furina - Genshin Impact
    \n#913 - Purple Heart - Hyperdimension Neptunia
    \n#914 - Norman - Yakusoku no Neverland
    \n#915 - Vermeil - Kinsou no Vermeil: Gakeppuchi Majutsushi wa Saikyou no Yakusai to Mahou Sekai wo Tsukisusumu
    \n#916 - Vivy - Vivy -Fluorite Eye's Song-
    \n#917 - Saiko Yonebayashi - Tokyo Ghoul
    \n#918 - Jewelry Bonney - One Piece
    \n#919 - Amadeus - Steins;Gate
    \n#920 - Kim Possible - Kim Possible
    \n#921 - Paimon - Genshin Impact
    \n#922 - Mari Makinami Illustrious - Rebuild of Evangelion
    \n#923 - Maple - BOFURI: I Don't Want to Get Hurt, so I'll Max Out My Defense.
    \n#924 - Marnie - Pokémon Sword/Shield
    \n#925 - Miles Edgeworth - Phoenix Wright: Ace Attorney
    \n#926 - White Queen - Date A Bullet
    \n#927 - Jigglypuff - Pokémon: Indigo League
    \n#928 - Helen Parr - The Incredibles
    \n#929 - Loona - Helluva Boss
    \n#930 - Meiko Shiraki - Prison School
    \n#931 - Sakamata Chloe - hololive
    \n#932 - Ferris - Re:Zero kara Hajimeru Isekai Seikatsu
    \n#933 - Priestess - Goblin Slayer
    \n#934 - MEM-Cho - 【OSHI NO KO】
    \n#935 - Alucard (CV) - Castlevania III: Dracula's Curse
    \n#936 - Xie Lian - Tian Guan Ci Fu
    \n#937 - Mukuro Ikusaba - Danganronpa: Trigger Happy Havoc
    \n#938 - Rick Astley - 🤔
    \n#939 - Alhaitham - Genshin Impact
    \n#940 - Koala - One Piece
    \n#941 - Noelle - Genshin Impact
    \n#942 - Miyuki Shiba - Mahouka Koukou no Rettousei
    \n#943 - Kou Minamoto - Jibaku Shounen Hanako-kun
    \n#944 - Takina Inoue - Lycoris Recoil
    \n#945 - Ty Lee - Avatar: The Last Airbender
    \n#946 - Coconut - Nekopara
    \n#947 - Duo - Duolingo
    \n#948 - Raynare - High School DxD
    \n#949 - Tomo Aizawa - Tomo-chan wa Onnanoko!
    \n#950 - Touka Takanashi - Chuunibyou demo Koi ga Shitai!
    \n#951 - Aquarius - Fairy Tail
    \n#952 - Komugi - Hunter × Hunter
    \n#953 - Makoto Yuki - Persona 3
    \n#954 - Honami Ichinose - Classroom of the Elite
    \n#955 - Tokino Sora - hololive
    \n#956 - Mabel Pines - Gravity Falls
    \n#957 - Chise Hatori - Mahoutsukai no Yome
    \n#958 - Suruga Kanbaru - Monogatari
    \n#959 - Miles 'Tails' Prower - Sonic the Hedgehog 2
    \n#960 - Garou - One Punch Man
    \n#961 - Elsa Granhiert - Re:Zero kara Hajimeru Isekai Seikatsu
    \n#962 - Sakura Yamauchi - Kimi no Suizou wo Tabetai
    \n#963 - Narancia Ghirga - JoJo's Bizarre Adventure: Golden Wind
    \n#964 - Charlotte Pudding - One Piece
    \n#965 - Jessie's Mimikyu - Pokémon the Series: Sun & Moon
    \n#966 - Jessica Rabbit - Who Framed Roger Rabbit
    \n#967 - Chel - The Road to El Dorado
    \n#968 - Lisbeth - Sword Art Online
    \n#969 - Emma Sano - Tokyo卍Revengers
    \n#970 - Melascula - Nanatsu no Taizai
    \n#971 - Mitsuru Kirijo - Persona 3
    \n#972 - Sousuke Mitsuba - Jibaku Shounen Hanako-kun
    \n#973 - Luigi - Super Mario Bros.
    \n#974 - Super Sonico - Nitroplus Mascots
    \n#975 - Moona Hoshinova - hololive
    \n#976 - The Joker - DC
    \n#977 - Kayo Hinazuki - ERASED
    \n#978 - Grayfia Lucifuge - High School DxD
    \n#979 - Undertaker - Black Butler
    \n#980 - Fyodor Dostoevsky - Bungou Stray Dogs
    \n#981 - Pyro - Team Fortress 2
    \n#982 - Marinette Dupain-Cheng - Miraculous: Tales of Ladybug & Cat Noir
    \n#983 - Narumi Momose - Wotaku ni Koi wa Muzukashii
    \n#984 - IA - VOCALOID
    \n#985 - Petra Ral - Attack on Titan
    \n#986 - Itsuki Sumeragi - Kakegurui
    \n#987 - Han Sooyoung - Omniscient Reader's Viewpoint
    \n#988 - SCP-3008 - SCP Foundation
    \n#989 - Rika Orimoto - Jujutsu Kaisen
    \n#990 - Jack the Ripper - Fate/Apocrypha
    \n#991 - Reimi Sugimoto - JoJo's Bizarre Adventure: Diamond Is Unbreakable
    \n#992 - Yelena - Attack on Titan
    \n#993 - Sadayo Kawakami - Persona 5
    \n#994 - Mia Khalifa - Mia Khalifa
    \n#995 - Aries - Fairy Tail
    \n#996 - Momosuzu Nene - hololive
    \n#997 - Chomusuke - Kono Subarashii Sekai ni Shukufuku wo!
    \n#998 - Donquixote Doflamingo - One Piece
    \n#999 - Neji Hyuuga - Naruto
    \n#1000 - Susamaru - Kimetsu no Yaiba"""

    topChars = {}

    for line in x.split("\n"):
        if line.count(" - ") != 2:
            print(line)
            continue
        rank = int(line.split(" - ")[0][1:].strip())
        name = line.split(" - ")[1].strip()
        origin = line.split(" - ")[2].strip()

        topChars[name] = {"rank":rank,
                          "name":name,
                          "series":origin}



    # db = Database("RoutedClaims.db")

    # db.cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    # tableNames = db.cursor.fetchall()
    # print(tableNames)

    # dbChars = {}
    # db.cursor.execute("SELECT * FROM CHARACTER_EMBEDS")
    # entries = db.cursor.fetchall()

    # for entry in entries:
    #     # print(entry)
    #     dbChars[entry[0]] = {"origin":entry[1], "value":entry[2], "img_url":entry[3]}

    # for char in topChars:
    #     if char in dbChars:
    #         print(char)
    #         IMAGE_CHARACTERS[char] = dbChars[char]

    # print(len(IMAGE_CHARACTERS))


    # max_entry = max(characters.items(), key=lambda x: x[1]['value'])
        
    # sorted_dict_values = sorted(characters.items(), key=lambda x: int(x[1]["value"]), reverse=True)

    






names = [key for key in topChars.keys()]

vectorizer = TfidfVectorizer(analyzer="word")
X = vectorizer.fit_transform(names)

print("Starting. . .")

while True:
    query = input("SearchName: ")

    if query == "EXIT":
        break

    query_vector = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vector, X)
    N = 3
    threshold = 0.3
    # Get indices of entries with similarity above threshold
    similar_indices = [i for i, score in enumerate(similarity_scores[0]) if score > threshold]

    # Retrieve similar strings and their similarity scores
    similar_strings_with_scores = [(names[i], similarity_scores[0][i]) for i in similar_indices]

    # Sort by similarity score (highest to lowest)
    similar_strings_with_scores.sort(key=lambda x: x[1], reverse=True)[N:]

    print("Ranked similar strings above threshold:")
    for string, score in similar_strings_with_scores:
        print(f"\t{string}: {score}")