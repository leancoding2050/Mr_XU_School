17/4/2025  
---
來總結做了甚麼  
在這項目中用了Django及nextjs來寫,Django是用來做存公共數據用,nextjs是用來Temaplate用
先說Django 
- 主檔案的名稱叫DJ_DB,之後有四個app分別叫course_data, school_branch_campus,school_data,user_role
(課程數據、學校分校、學校數據、使用者角色)
- 在requirements.txt中,是用了annotated-types==0.7.0
asgiref==3.8.1
contextlib2==21.6.0
Django==4.2
django-cors-headers==4.4.0
django-ninja==1.3.0
django-ninja-extra==0.21.4
injector==0.22.0
psycopg2-binary==2.9.9
pydantic==2.9.2
pydantic_core==2.23.4
sqlparse==0.5.1
typing_extensions==4.12.2

- 整個Django api是用了django-ninja

---
到了nextjs  
---
  "dependencies": {
    "@auth/prisma-adapter": "^2.6.0",
    "@fullcalendar/core": "^6.1.15",
    "@fullcalendar/daygrid": "^6.1.15",
    "@fullcalendar/interaction": "^6.1.15",
    "@fullcalendar/multimonth": "^6.1.15",
    "@fullcalendar/react": "^6.1.15",
    "@fullcalendar/rrule": "^6.1.15",
    "@fullcalendar/timegrid": "^6.1.15",
    "@hookform/resolvers": "^3.9.0",
    "@prisma/client": "^5.20.0",
    "@radix-ui/react-checkbox": "^1.1.2",
    "@radix-ui/react-dialog": "^1.1.7",
    "@radix-ui/react-icons": "^1.3.0",
    "@radix-ui/react-label": "^2.1.0",
    "@radix-ui/react-popover": "^1.1.2",
    "@radix-ui/react-select": "^2.1.2",
    "@radix-ui/react-slot": "^1.1.0",
    "@radix-ui/react-switch": "^1.1.2",
    "axios": "^1.7.7",
    "bcryptjs": "^2.4.3",
    "class-variance-authority": "^0.7.0",
    "cloudinary": "^2.5.1",
    "clsx": "^2.1.1",
    "date-fns": "^3.6.0",
    "lucide-react": "^0.451.0",
    "next": "14.2.14",
    "next-auth": "^5.0.0-beta.22",
    "next-cloudinary": "^6.16.0",
    "next-connect": "^1.0.0",
    "prisma": "^5.20.0",
    "react": "^18",
    "react-day-picker": "^8.10.1",
    "react-dom": "^18",
    "react-hook-form": "^7.53.0",
    "react-modal": "^3.16.1",
    "react-multi-date-picker": "^4.5.2",
    "react-pdf": "^9.2.1",
    "react-router-dom": "^6.27.0",
    "sonner": "^2.0.3",
    "swr": "^2.2.5",
    "tailwind-merge": "^2.5.3",
    "tailwindcss-animate": "^1.0.7",
    "zod": "^3.23.8",
    "zustand": "^5.0.3"
  },
  "devDependencies": {
    "@types/bcryptjs": "^2.4.6",
    "@types/formidable": "^3.4.5",
    "@types/multer": "^1.4.12",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "@types/react-modal": "^3.16.3",
    "eslint": "^8",
    "eslint-config-next": "14.2.14",
    "postcss": "^8",
    "tailwindcss": "^3.4.1",
    "typescript": "^5"
  }
用了以上的lib

- 在項目中我開了9個文件夾
- actions (serveraction)
- app (前端Template)
- components (用在Template)
- data (authjs-V5的找用戶 db function)
- lib (放一些hook function)
- middle-role (在authjs-V5中用的權限分類用)
- prisma (寫prisma db用(自動生成))
- public (主要在loacl開發時存相片)
- schemas (是用來寫login 的schema)

之後有幾個文件比較重要,分別.env,auth.config.ts,auth.js,middleware.ts,next.config.mjs

- .env (是用postgres DB 遲點用  阿里云的db服務)

- auth.config.ts (是authjsV5的自定登入設定 可分成著通用戶 及 職員用戶登入)

- auth.ts (是整個authjsV5的function核心)

- middleware.ts ( 是來控制那些頁面可以在沒有登入情況(token)下能去到 )

- next.config.mjs (在第三方的api進入來時,加入用的用來看由第三方傳來的數據)

----

先說說這項目的思路
---

 正如以上所說,這網站是有兩種身分登入(在nextjs中),分別為職員及普通用戶.

- 職員可分為老師,管理員(小),管理員(大)

- 用戶可分為 家長

- 管理員(大)可以做的有,審查申請,課程管理,公告管理,筆記管理,商品管理,學校管理,假期管理,老師薪酬管理,時間模版管理,家長繳費提示管理,用戶管理,筆記管理(隱藏,後補)

- 管理員(小)(隱藏,後補)可以做的有,審查申請,課程管理,公告管理,筆記管理,商品管理,學校管理,假期管理,時間模版管理,家長繳費提示管理,用戶管理,筆記管理(隱藏,後補)

- 老師 可以做的有 點名,上傳筆記 在學生的資料中留下評論

- 家長 可以做的有 學生管理(子女), 申請系統(首堂,加堂,掉堂)
    - 學生(上傳資料)

而Django部份是有一個superuser來管理公共資料

----
管理員(大)/管理員(小)
---

- 審查申請
    - 類型
        - 申請
        - 加堂
            - 接受
            - 拒絕

- 課程管理
    - 修改課程
    - 加入學生
    - 建立課堂
        - 修改課堂
        - 加堂
        - 掉堂

- 公告管理
    - 建立公告
    - 修改公告

- 筆記管理
    - 上傳筆記

- 商品管理
    - 建立商品

- 學校管理
    - 建立學校
        -建立學校資訊
        - 上傳時間表
        - 上傳考試時間表
        - 上傳書單
        - 上傳考試範圍表
        - 上傳考試卷
        - 上傳學校時間表

- 假期管理
    - 建立假期
    - 修改假期

- 老師薪酬管理
    - 只查看

- 時間模版管理
    - 建立時間模版
    - 修改時間模版

- 家長繳費提示管理
    - 只有output

- 用戶管理
    - 建立家長
        - 建立學生
        - 修改學生
    - 建立老師
    - 修改老師
    - 建立管理員
    - 修改管理員

- 筆記管理
    - 建立筆記


老師
---
- 點名
    - 學生點名

- 上傳筆記
- 在學生的資料中留下評論
    - 建立評論
    - 修改評論

家長
---

-  學生管理(子女)
    - 建立學生(子女)
        - 建立學生(子女)資料
           
            - 上傳時間表
            - 上傳考試時間表
            - 上傳書單
            - 上傳考試範圍表
            - 上傳考試卷
            - 上傳學校時間表
- 申請系統
    - 首堂
    - 加堂
    - 掉堂

---
整個nextjs用了shadcn zod prisma react-hook-form server-action

---
login
---
用了authjs V5


審查申請
---
要有家長配合都可以運作成功,  
首沖(首堂)  流程是,家長(商城)->單個物品->申請按捏->進入admin申請表->admin審核->接受->家長繳費提示管理(列表)

加堂/掉堂 加堂是在考試前一個月會在家長某位置問(理想) ,掉堂不知 whatapps(可能?)
    ? -> 進入admin申請表->admin審核->接受->家長繳費提示管理(列表)

麻煩的位置是code層面,都是與申請相關的model中field 狀態不停更新


課程
---
部分,要建立課程前先要做一些步驟,先建立時間模版又怎樣做
1. 先建立公眾假期(react-multi-date-picker中的DatePicker主要用這東西來選擇日子,type是string)一年內
   - 有bug:可能要改成當有DATA時,不能再生成新DATA,而是update DATA (之後看看) 
2. 建立時間模版,在建立時間模版中,會讀取公眾假期數據,想法用戶先選了開始日子,及結束日子,之後在這段時間設定時間模式,并輸入年級,開始時間,結束時間,以及有多少節數和模組名
    - 節數與筆記有關
3. 建立課堂,可以先選取早前所建立的時間模版,之後用補選課程名,人數(與筆記數量有關),課室,老師(可選)


說說課堂是怎樣生成,這個是比較煩及複雜的因為是跟據model Course中的field day(自選日子) 及 field weekday(每週重複) 來決定課堂的數量,之後承繼著model中的年級,開始時間,結束時間,節數是自動生成,人數,課室,老師,學生  
在這基本說說code的寫法  
苜先其實整個建立課堂都是自動生成出來,field day(自選日子) 及 field weekday(每週重複)因為在formdata是type是obj,之後要在把type轉換成Array,之後map()field day(自選日子) 及 field weekday(每週重複)兩組日子合一,之後再用合併了的一組日子來loop create class function大概是這樣  


公告
---
都是一些基本東西,沒有太特別的

商品
---
都是一些基本東西,沒有太特別的

學校
---
這個學校是用來建立學生時必用的,所以在建立學生前應該先要建立學校先.
在操作層面下學校都是複雜,學校要上傳很多資料(
- 上傳時間表
- 上傳考試時間表
- 上傳書單
- 上傳考試範圍表
- 上傳考試卷
- 上傳學校時間表
),  
分類跟據, 
- 科目,
- 季度,
- 年份,
- 年級  ,
但是像俄羅斯套娃般來打開要想的東西這樣說好像很簡單
,
在寫code層面跟操作都是一樣煩亂,要跟據param,來做url,每做一頁寫一次
在api方面小心留意param的值名字

用戶管理
---
這個是難度一般,可以建立老師,管理員(小),家長,(學生 ,學生沒有用戶)用戶,
code層面沒有太煩想法

---

家長
---
商城
在管理員所說的差不多,不過有不同的事商城之後的不是比錢,而是申請系統

申請
---
未做

上傳
---
跟上面一樣,但是有點于一樣,學生跟學校所上傳的表面一樣,但內裹用的DB model名不是一樣


老師
---
上傳筆記
未做

點名
---
這個真是真分D麻煩事,因為所影響的model太大,先要找出該課堂,之後內的學生列表,按制,接完不能再按
接完之後,進行老師薪水更新
這簡單的一串動作,已影響了學生出席,老師薪水,課堂機制等等model不過最煩都是前端問題

在學生的資料中留下評論
---
基本,勿6
