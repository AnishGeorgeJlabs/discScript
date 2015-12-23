height_range = ['5\'1\"', '5\'2\"', '5\'3\"', '5\'4\"', '5\'5\"', '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10',
                '5\'11', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"', '6\'4\"', '6\'5\"', '6\'6\"']

color_list = [" antique gold ", " antique-gold ", " antique silver ", " antique-silver ", " aqua blue ", " aqua-blue ",
              " navy blue ", " navy-blue ", " brick red ", " brick-red ", " camel shade ", " camel-shade ",
              " grey milange ", " grey-milange ", " charcoal grey ", " charcoal-grey ", " cobalt blue ", " dark grey ",
              " dark-grey ", " grey milange ", " ice blue ", " ice-blue ", " light blue ", " light-blue ",
              " light grey ", " light-grey ", " mustard yellow ", " mustard-yellow ", " off white ", " off-white ",
              "  steel grey ", " two tone ", " two-tone ", " violet indigo ", " violet-indigo ", " white ", " wine ",
              " yellow ", " antique ", " apricot ", " aqua ", " ash ", " assorted ", " olive ", " orange ", " peach ",
              " pearl ", " pink ", " purple ", " red ", " ruby ", " rust ", " sand ", " silver ", " beige ", " black ",
              " blue ", " champagne ", "  bronze ", " brown ", " camel ", "  cherry ", " citrine ", " coffee ",
              " copper ", " cream ", " emerald ", " firozi ", " fuchsia ", " golden ", " green ", " grey ", " ice ",
              " ivory ", " khakhi ", " khaki ", " lavender ", " lemon ", " lilac ", " magenta ", " maroon ", " mauve ",
              " metal ", " milange ", " multi ", " tan ", " transparent ", " turquoise ", " neutral ", " nude "]
# old color list we are not using it now
color_list1 = [" purple ", " brick red ", " brick-red ", " ice blue ", " aqua blue ", " aqua-blue ", " light grey ",
               " light-grey ", " ice-blue ", " navy blue ", " navy-blue ", " ivory ", " violet indigo ", " off white ",
               " off-white ",
               " apricot ", " transparent ", " camel ", " lilac ", " emerald ", " cream ", " silver ", " grey milange ",
               " grey-milange ",
               " charcoal grey ", " charcoal-grey ", " light blue ", " light-blue ", " antique silver ",
               " antique-silver ", " dark grey ", " dark-grey ",
               " coffee ", " firozi ", " blue ", " green ", " golden ", " assorted ", " rust ", " pink ", " turquoise ",
               " olive ",
               " two tone ", " two-tone ", " grey ", " peach ", " nude ", " sand ", " pearl ", " red ", " copper ",
               " champagne ",
               " bronze ", " brown ", " mustard ", " yellow ", " multi ", " maroon ", " neutral ", " aqua ",
               " camel shade ",
               " fuchsia ", " beige ", " magenta ", " khaki ", " lemon ", " ruby ", " black ", " lavender ", " yellow ",
               " wine ", " cherry ", " white ", " khakhi ", " antique ", " mauve ", " metal ", " tan ", " orange "]
# material list
shadecard_bricks = ["eye pencil", "eye shadow", "lip liner", "eye liner", "lipstick", "lips gloss", "make-up base",
                    "nail enamel", "mascara", "compact powder", "blusher",
                    "lip balm", "lip care", "loose powder", "concealer & corrector", "face highlighter", "highlighter",
                    "nail art", "kajal", "nail top & base coat", "eye palette"]
beauty = ["strech denim"]  # beauty and fragnances
toys = ["100% linen"]
Actsprts = ["polyester", "polyester spandex", "poly cotton"]
home = ["100% cotton", " velvet", " taffeta", " 100% satin cotton", " cotton", " silk", " polyester", " polycotton",
        " polypropylene", " 65% polyester 35% cotton", " pvc", " outer cotton inner polyester", " wood", " rubber",
        " 80%cotton 20%polyester", " 100% cotton with poly filling", " polyster", " polysilk", " nylon", " viscose",
        " terry", " jute", " poly velvet", " wool", " cotton blend", " 100% polyester", " poly dupion",
        " polyester viscose", " linen", " cotton silk", " polyester wool", " 100% cotton with polyfill", " chenille",
        " na", " microfibre", " micro fabric", " micro fibre", " ceramic", " suede", " fibre", " soyabean",
        " polyester filling", " metal", " rayon", " tencel", " cotton vicsose", " microfibre filling",
        " 70%cotton 30%polyester", " 60% viscose 40% polyester", " 65%polyester 35%viscose", " polyester satin",
        " leatherette", " 100% mercerized cotton", " spandex", " plastic", " cotton satin",
        " cotton blend with polyfill", " poly viscose", " 70%polyester 30%cotton", " fleece", " 60%cotton 40%polyester",
        " 60%polyester 40%cotton", " iron", " stainless steel", " memory foam"]

jewellery = ["silver", " alloy", "brass metal", " copper", " 92.5 silver", " 92.5 sterling silver", " brass",
             " glass beads", " german silver", " beads", " resin", " thread", " 18 karat gold", " faux leather",
             " bones", " acrylic", " wooden", " stone", " stainless steel", " sterling silver", " metal", " plastic",
             " lace", " leather", " shell", " brass & leather", " nylon", " brass & beads", " clay", " fabric",
             " 14 karat gold", " gold", " wood", " pewter", " silver+alloy", " alloy & acrylic", " pearl", " tungsten",
             " crystal", " pu", " semi-precious stones", " swarovski elements", " polyester", " ceramic", "titanium",
             " steel", " 316l stainless steel", " na", " 80%metal, 20%glass", " 69%steel, 40%acrylic", " copper alloy",
             " 100%zinc", " cz", " diamond", " bronze", " metal/leather", " leather/brass", " leather/beads"]

acc = ["pu", " leather", " jute", " fabric", " dupion silk", " shimmer", " brocade", " 100% polyurethane", " cotton",
       " polyester", " velvet", " polyurethane", " silicon", " resin", " polyamide", " non leather", " polycarbonate",
       " canvas/leather", " brass", " faux leather", " nylon", " plastic", " silk", " metal", " stainless steel",
       " rubber", " alloy", " tetron", " polypropylene", " pvc", " dobby nylon", " 600d polyester", " ripstop fabric",
       " presspro technology", " leatherette", " acetate", " cloth", " synthetic leather", " net", " fibre",
       " cotton canvas", " tatron", " suede", " synthetic", " cuzy nylon fabric",
       " lightweight and tough polycarbonate", " premium polynlyon fabric", " polyester fabric", " twill fabric",
       " tough polyester fabric", " ceramic", " shell", " canvas", " stylish printed jaquard fabric",
       " tough polypropylene shell", " premium diamond ripstop fabric", " sheet", " tough polypropylene", " wood",
       " wool", " tr-90", " steel", " 900d polyester", " neoprene", "titanium", " raw silk", " lacquer",
       " artificial leather", " satin", " denim", " canvas/pu", " vegan cow leather", " aluminium", " 1680d polyester",
       " poly", " flex", " poly/shimmer", " poly shantoon/shimmer", " pearl", " daneir fabric", " acrylic", " others",
       " canvas & leather", " 420d nylon", " acetate blend", " 900d polyester x 600d polyester",
       " nylon honeycomb x 600 d polyester", " webbing", " propionate", " viscose", " cotton silk", " wooden",
       " textreme 6.6", " 450 hd polyoxford", " t-square rip", " t-rip light", " 210t nylon ripstop", " texamid 11.1",
       " canvas and leather", " plastic moulded footwear", " 80% wool 20% nylon", " 630d polyester + 420d dobby", " na",
       " pu/canvas", " fur", " alloy & acrylic "]

apparels = ["chiffon", " cotton", " cotton blend", " crepe", " poly georgette", " polyester", " viscose",
            " polyester blend", " poly crepe", " 100% cotton", " cotton spandex (stretchable)", " 100% polyester",
            " 100% acrylic", " woolen", " georgette", " silk", " cotton silk", " cambric", " silk blend",
            " banarsi silk", " chanderi", " polyamide", " cotton spandex(stretchable)", " banarasi", " net", " velvet",
            " brocade", " poly chiffon", " chanderi silk", " acrowool", " poly silk", " satin", " cotton rich",
            " polyamide blend", " pu", " polyester spandex", " super net", " 95%polyester 5%spandex(stretchable)",
            " 90%polyester 10%spandex(stretchable)", " cotton polyester", " polyester cotton", " polyester georgette",
            " jaquard", " leather", " polycotton", " denim", " corduroy", " 80% acrylic, 20% cotton", " jersey",
            " rayon", " acrylic wool", " chanderi cotton", " knit", " wool rich", " linen blend", " acrylic blend",
            " nylon", " polyster", " 100% viscose", " 96%polyester 4%spandex(stretchable)", " cotton viscose", " pique",
            " stretch cotton", " cotton poly spandex", " 95/5 cotton lycra", " cotton polyamide spandex(stretchable)",
            " 92%cotton 8%spandex(stretchable)", " polyamide spandex", " micro fibre", " poly", " cotton poly",
            " 95%viscose 5%spandex(stretchable)", " polyester spandex(stretchable)", " rayon blend", " others",
            " viscose spandex", " linen", " cotton & denim", " viscose blend", " poly viscose", " poly cotton", " wool",
            " acrylic", " 100% organic cotton", " crepe jersey", " cotton satin", " 60%cotton 40%polyester",
            " polyester lycra", " cotton linen", " brasso", " cotton 97% elastane 3%", " cotton jersey",
            " 95%cotton 5%spandex(stretchable)", " cotton knit", " elastane(stretchable)", " canvas", " art silk",
            " net and jacquard", " cotton stretch", " fleece", " 95% cotton 5% spandex", " 98% cotton 2% spandex",
            " net and georgette", " cotton voile", " 80%viscose 13%nylon 7%spandex(stretchable)", " net and brasso",
            " rayon spandex(stretchable)", " rayon polyester", " viscose lycra", " polyester crepe", " jersy",
            " polyamide spandex(stretchable)", " viscose spandex(stretchable)", " synthetic stretch",
            " nylon spandex(stretchable)", " 96%viscose 4%spandex(stretchable)", " 95%terelene 5%spandex(stretchable)",
            " terry rayon", " modal", " jute", " polyester viscose spandex(stretchable)", " actylic", " tissue",
            " organic cotton", " dupion silk", " poly linen", " poly wool", " flannel", " metal", " raw silk",
            " bamboo", " jacquard crepe", " polyster chiffon", " nylon blend", " wool blend", " linen cotton",
            " net jacquard", " sequins fabric", " 100% linen", " poly rayon spandex", " 92/8 viscose lycra",
            " poly viscose elastane", " cotton modal", " organza", " synthetic", " micro", " poly satin",
            " nylon lycra", " 100% nylon", " lyocell", " chambrey", " tweed", " tussar", " microfibre", " shimmer",
            " cotton fleece", " modal blend", " bamboo organic cotton blend", " viscose modal", " cotton rayon",
            " polyurethane", " viscose jersey", " bhagalpuri silk", " strech denim", " blended",
            " cottonpoly spandex(stretchable)", " artificial silk", " polyester viscose", " linen/cotton",
            " tussar silk", " organic cotton spandex", " nylon spandex", " bamboo cotton blend",
            " organic cotton eucalyptus blend", " viscose jersy", " cotton satin spandex(stretchable)", " twill",
            " twill lycra", " steel", " 100% cotton poplin", " shantoon", " velour", " terelyne rayon",
            " net and chiffon", " gorgette", " 100% polyurethane", " faux leather", " crepe silk", " cotton lawn",
            " poly viscose wool", " 80% cotton, 20% polyester", " 60% cotton/40% polyester",
            " cotton 85% viscose 10% elastane 5%", " bamber", " tencel", " brass", " 80% cotton, 20% wool",
            " 80%cotton 20%polyester", " 80% acrylic 20% wool", " ramie", " denim spandex(stretchable)", " alloy",
            " viscose silk", " 87% nylon + 13% lycra(elastane)", " polyester silk", " 100% wool", " net brasso",
            " net and  georgette", " crochet", " teflon", " poly dupion", " mesh", " net and silk", " 100%cotton",
            " viscose jacquard", " cvc", " dobby", " handloom silk", " poly viscose nylon",
            " wool cotton spandex(stretchable)", " pvc", " leatherette", " micro poly blend",
            " twill spandex(stretchable)", " polyester fleece", " suede", " combed cotton", " 50%cotton 50%polyester",
            " nylon & cotton", " sheer", " woven", " 60/40 polycotton", " acetate blend", " bamberg",
            " 75%polyester 23%viscose 2%lycra", " tafetta", " taffeta", " 80/20 cotton wool",
            " polycotton spandex(stretchable)", " 65%polyester 35%viscose", " chandelier lace", " polyester satin",
            " 95% polyester 5%spandex", " silicon", " 65%polyester,35%cotton", " polyester nylon", " polyester chiffon",
            " poplin", " georgette crepe", " brocade silk", " fur", " jute silk", " cotton 96% elastane 4%",
            " polyknit spandex(stretchable)", " acetate", " brasso silk", " flex", " plastic", " twill spandex",
            " beads", " cotton 98% elastane 2%", " 60% polyester, 40% cotton", " 70% cotton, 30% polyester",
            " 100%viscose", " terry"]

no_vitals = ["belt", "boxers", "briefs", "caps", "combo", "cufflinks", "handkerchief", "hats", "mufflers", "scarves",
             "socks", "ties", "trunks", "vests", "wallet", "wristbands", "dupattas", "shawls", "shrugs", "stoles",
             "pocket square"]

upper_material = ["genuine leather", "suede leather", "mesh, synthetic leather", "synthetic", "breathable nylon mesh",
                  "non leather", "nylon mesh", "mesh", "breathable mesh", "rubber like (eva)",
                  "air mesh", "canvas", "patent leather", "genuine leather/canvas", "polyester mesh", "nubuck leather",
                  "mesh suede leather", "welded overlays mesh", "rubber", "satin", "synthetic mesh",
                  "velvet", "suiede mesh", "canvas/genuine leather", "croslite", "eva", "leather", "satin fabric",
                  "synthetic suede leather", "60% genuine leather, 40% textile", "engineered mesh",
                  "jute", "micro suede/mesh"]
footwear_mat = ["plastic moulded footwear", "cotton", "pvc", "non leather", "leather", "na"]
sole_material = ["tpr", "leather", "rubber", "rubber like (eva)", "pu", "pvc", "phylon", "eva", "resin sheet", "airmax",
                 "tpu", "cork", "croslite", "crape", "non marking rubber"]

# color maps
grey = [" charcoal grey ", " charcoal-grey ", " dark grey ", " dark-grey ", " light grey ", " light-grey ",
        "  steel grey ", " grey "]
silver = [" antique silver ", " antique-silver ", " silver "]
red = [" brick red ", " brick-red ", " red "]
milange = [" grey milange ", " grey-milange ", " grey milange ", " milange "]
white = [" off white ", " off-white ", " white "]
antique = [" antique gold ", " antique-gold ", " antique "]
blue = [" aqua blue ", " aqua-blue ", " navy blue ", " navy-blue ", " cobalt blue ", " cobalt-blue ", " ice blue ",
        " ice-blue ", " light blue ", " light-blue ", " blue "]
yellow = ["mustard yellow ", " mustard-yellow ", "yellow "]

neck_list = [" crew neck ", " round neck ", " polo neck ", " v neck ", " mandarin collar ", " henley neck ",
             " halter neck ", " asymmetric neck ", " keyhole neck ", " hooded neck ", " square neck ", " boat neck ",
             " shawl collar ",
             " collar neck ", " spaghetti neck ", " scoop neck ", " high neck ", " nehru collar ", " sweetheart neck ",
             " lapel collar ", " open neck ", " bow tie neck ", " cowl neck ", " mock neck ", " peter pan collar ",
             " notch collar ", " round neck ", " turtle neck ", " comfort neck ", " chinese neck with collar ",
             " bow neck ", " kimono neck ", " button ", " band collar ", " straight collar "
             ]
sleeves_list = ["half sleeve", "sleeve less", "3/4th sleeve", "full sleeve", "cap sleeve", "butterfly sleeve",
                "puffed sleeve", "raglan sleeve", "short sleeve", "roll up sleeve", "ruffle sleeves",
                "poncho", "ruffle sleeve", "mega sleeves", "quarter sleeve", "dolman sleeve", "mega sleeve",
                "bell sleeve", "long sleeve", "kimono", "drop shoulder", "drape sleeve",
                "double cuff", "full sleeve with double cuff"]
closing_list = ["slip on", "lace-up", "unspecified", "velcro", "open / slipper", "buckle", "zip", "open/slipper",
                "rinsed effect", "quartz", "15 inches", "washed effect", "16 inches", "14 inches", "10 inches",
                "12 inches", "enzyme wash effect"]
linning_list = ["leather", "fabric", "non leather", "mesh", "synthetic", "rubber like (eva)", "uv protected", "yes",
                "polarised", "plain", "croslite", "polycarbonate", "printed", "embroidered", "velvet", "jacquard"
                ]
fit_list = [" regular fit ", " flared fit ", " loose fit ", " slim fit ", " skinny fit ", " straight fit ",
            " narrow fit ", " pencil fit ", " relaxed fit ", " comfort fit ", " regular-fit ", " flared-fit ",
            " loose-fit ", " slim-fit ", " skinny-fit ", " straight-fit ", " narrow-fit ", " pencil-fit ",
            " relaxed-fit ", " comfort-fit "]
style_list = [" printed ", " pleated ", " embellished ", " stripes ", " solids ", " embroidered ", " color blocked ",
              " floral ", " self pattern ", " checks ", " a line ", " straight ", " anarkali ",
              " non wired-non padded ", " underwired-non padded ", " underwired-padded ", " solid color ", " washed ",
              " shift dress ", " bodycon dress ", " skater dress ", " self patten ", " dobby ", " patiala ", " knit ",
              " flared ", " non wired-padded ", " asymmetric ",
              " asymmetric dress ", " sequins ", " a-line ", " off shoulder ", " elasticated ", " graphic ",
              " patch work ", " stoles ", " pintucks ", " maxi dress ", " low rise ", " padded ", " cardigans ",
              " hipster ", " sports bra-non padded ", " bomber ", " high waist ", " jacquard ", " tie & dye ",
              " bikini ", " melange ", " hoodie ", " flat knit ", " draped ", " strappy ", " wrap ", " unstitched ",
              " thong ", " baggy ", " tights ", " drawstring ", " ethnic ",
              " quilted ", " mid rise ", " medium waist ", " high rise ", " low waist ", " mid waist ", " skd ",
              " legging "]
heelshape_list = [" flat ", " wedge ", " stiletto ", " cone ", " kitten ", " block ", " platform ", " other ",
                  " stacked "]
length_list = [' thigh length ', ' hip length ', ' knee length ', ' mini ', ' waist length ', ' ankle length ',
               ' full length ', ' calf length ', ' regular length ', ' 3/4th length ', ' short  ', ' cropped length ',
               ' maxi ', ' mini/short ', ' midi ', ' maxi/long ', ' 50 m ', ' 29 inches ', ' mid-thigh length ',
               ' regular length socks ', ' ankle length socks ', ' midi/calf length ', ' 42 inches ']

## God knows why this is here
'''material_details=["95%terelene 5%spandexstretchable","450 hd polyoxford","polyester + nonwoven","100% cotton with poly filling","90%polyester 10%spandexstretchable","92%cotton 8%spandexstretchable","92/8 viscose lycra","96%polyester 4%spandexstretchable","60% cotton/40% polyester","96%viscose 4%spandexstretchable","92%rayon 8%spandexstretchable","75%polyester 23%viscose 2%lycra","cotton 85% viscose 10% elastane 5%","cotton polyamide spandexstretchable","80% acrylic 20% wool",
"cotton","pu","chiffon","cotton spandex stretchable","leather","crepe", "poly georgette","polyester blend","100% cotton","100% polyester","brocade","knit","cotton blend",
"polyester","poly crepe","100% acrylic","chanderi","georgette","net","silk blend","crepe silk","92.5 silver","copper","alloy","jaquard","super net","silk","fabric","dupion silk",
"velvet","faux leather","brass metal","banarasi","viscose","na","polyester georgette","poly chiffon","chanderi cotton","polyamide","poly silk","brass","glass beads","german silver",
"denim","cotton satin","linen","cotton & denim","polycarbonate","silicon","rubber","shimmer","resin","satin","nylon","polycotton","cotton polyester","cotton rich","non leather",
"polyamide blend","jute","60%cotton 40%polyester","polyester lycra","cotton poly spandex","polyester spandex","100% polyurethane","banarsi silk","beads","95%cotton 5%spandexstretchable",
"net and jacquard","viscose blend","thread","metal","canvas/leather","polyurethane","plastic","stainless steel","corduroy","cotton viscose",
"poly cotton","canvas","18 karat gold","bones","polyester cotton","cotton knit","acrylic","linen/cotton","net and brasso","rayon","micro fibre","cotton spandexstretchable",
"linen blend","cotton linen","stretch cotton","micro","modal","jersey","tetron","95% cotton 5% spandex","woolen","95/5 cotton lycra","polypropylene",
"dobby nylon","lightweight and tough polycarbonate","tough polyester fabric","ripstop fabric","premium polynlyon fabric","presspro technology","polyamide spandex","95%polyester 5%spandexstretchable","cotton poly",
"95%viscose 5%spandexstretchable","rayon blend","viscose spandexstretchable","others","100% viscose","viscose spandex","leatherette","wood","cambric","80% acrylic, 20% cotton","pique",
"wooden","cotton canvas","cuzy nylon fabric","poly viscose","tough polypropylene","92.5 sterling silver","sterling silver","crepe jersey","premium diamond ripstop fabric",
"stylish printed jaquard fabric","polyester fabric","suede",
"poly","rayon spandexstretchable","viscose lycra","chanderi silk","acetate","shell","artificial silk","tough polypropylene shell","stone","ceramic","wool","polyester spandexstretchable","nylon blend","jersy","polyester viscose spandexstretchable",
"acrylic blend","mesh","raw silk","cotton voile","synthetic","lace","acrowool","neoprene","feather","cotton silk","cotton stretch","98% cotton 2% spandex",
"brass & leather","bamboo","brasso","synthetic leather","cloth","plastic moulded footwear","tissue","100% linen","100% organic cotton","net jacquard","cotton jersey","polyster chiffon","cotton 97% elastane 3%","pvc","outer cotton inner polyester","fleece","100% satin cotton",
"organic cotton","khadi cotton","twill fabric","synthetic stretch","65% polyester 35% cotton","polyester crepe","blended","sheet","poly rayon spandex","optyl","brass & beads","organza","net and silk","bhagalpuri silk","elastic","gold","14 karat gold","microfibre","cotton modal","eastman tritan",
"polyster","net brasso","tr-90","titanium","steel","wool blend","elastanestretchable","cotton fleece","600d polyester","900d polyester","tarapaulin","modal blend","bamboo organic cotton blend",
"poly linen","nylon spandex","strech denim","80%cotton 20%polyester","micro poly blend","cotton satin spandexstretchable","wool rich","polysilk","iron","multifilament","jacquard crepe","polycotton spandexstretchable","polyester viscose","polyamide spandexstretchable",
"organic cotton spandex","tussar silk","tussar","artificial leather","net and chiffon","poly satin","twill lycra","viscose jersy","rayon polyester","poly wool","viscose jersey",
"twill","nylon spandexstretchable","poplin","pewter","poly viscose elastane","fibre","dobby","net and georgette","shantoon","silver+alloy","cotton rayon","terry","terelyne rayon",
"aluminium","80% cotton, 20% polyester","sequins fabric","bamber","cotton lawn","65%polyester 35%viscose","bamboo cotton blend","organic cotton eucalyptus blend","tencel",
"chambrey","vegan cow leather","terry rayon","viscose modal","ramie","87% nylon + 13% lycraelastane","1680d polyester","gorgette","nylon & cotton",
"poly velvet","poly dupion","georgette brocade","alloy & acrylic","100% cotton with polyfill","denim spandexstretchable","flex","poly/shimmer","teflon","poly shantoon/shimmer",
"pearl","net and  georgette","polyester silk","brasso georgette","viscose jacquard","acrylic wool","crochet","vinyl","twill spandexstretchable","polyester fleece",
"monel","sheer","nylon & denim","60/40 polycotton","canvas & leather","acetate blend","bamberg","micro fabric","taffeta","chandelier lace",
"metal + plastic","cottonpoly spandexstretchable","polyester satin","cotton vicsose","semi-precious stones","100% nylon","linen cotton","polyester chiffon","100% cotton poplin","silver","100% organic cotton pique","65%polyester,35%cotton","swarovski elements",
"tungsten","316l stainless steel","georgette crepe","textile","69%steel, 40%acrylic","80%metal, 20%glass","graphite","composite","cotton 96% elastane 4%","webbing",
"poly viscose wool","80/20 cotton wool","schiffli","100% wool","copper alloy","printed cambric","100%zinc","jute silk","chenille","70%cotton 30%polyester","50%cotton 50%polyester",
"brasso silk","velour","crystal","lacquer","60% viscose 40% polyester","70% viscose 30% polyester","foam","twill spandex","100% mercerized cotton","porcelain","spandex","t-rip light",
"tarpaulin 1000","textreme 6.6","t-square rip","texamid 11.1","210t nylon ripstop","t-spun rip","420d nylon","65/35 polycotton pu","tweed","canvas and leather",
"polyester nylon","70%polyester 30%cotton","60%polyester 40%cotton","metal/leather","80% wool 20% nylon","cotton 98% elastane 2%","fabric/leather","canvas and faux leather","80%viscose 13%nylon 7%spandexstretchable","1680d nylon",
"soft denim","630d polyester + 420d dobby","leather/weebing","pu/canvas","leather/brass","metal plastic combo"]
'''
