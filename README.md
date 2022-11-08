# Заметки

##### vue| Урок 1/8. Создание сборки Vue приложения с использованием Node.js и Vue Cli 3 (хочу)
https://www.youtube.com/watch?v=22W54aRGr3Q&list=PLb6TvuNosCJW_N3wqAUYsp7DvUzfyvbvB

##### vue| How to install VUE CLI 3
https://www.youtube.com/watch?v=zACyNOlanXw

##### vue| install vue 
    установка
    vue create <name>
        manually
        Vuex, Router, Babel
        History mode
        config.json

##### vue| не работал роутер
    забыл добавить <router-view/> в app

##### vue+django| загрузка файлов img 
vue

"Загрузка файлов с помощью VueJS и Axios" https://webdevblog.ru/zagruzka-fajlov-s-pomoshhju-vuejs-i-axios/

django

"File upload with Django REST Framework" https://www.goodcode.io/articles/django-rest-framework-file-upload/

как сохранять a = Model(img=img) ... a.save()

"Unable to upload image to Django Project, getting Form object has no attribute 'save'" https://stackoverflow.com/questions/59837348/unable-to-upload-image-to-django-project-getting-form-object-has-no-attribute

другой подход

"HomeDjangoUploading file using API in Django Rest Framework
Uploading file using API in Django Rest Framework"
https://blog.vivekshukla.xyz/uploading-file-using-api-django-rest-framework/

##### vue| send post in axios
"axios post request to send form data" https://stackoverflow.com/questions/47630163/axios-post-request-to-send-form-data

##### vue| send data i ger query
"Send object with axios get request [duplicate]"

https://stackoverflow.com/questions/46404051/send-object-with-axios-get-request

    axios.get('/api/updatecart', { params: { product: this.product } }).then(...)

##### vue| push in vue
"TypeError: this.$route.push is not a function vue.js and Uncaught TypeError: Cannot read property 'push' of undefined" https://stackoverflow.com/questions/53340049/typeerror-this-route-push-is-not-a-function-vue-js-and-uncaught-typeerror-can

##### django| get query param by django
"How to access get request data in django rest framework" https://stackoverflow.com/questions/58207014/how-to-access-get-request-data-in-django-rest-framework

    test_data_var = request.query_params['testData']

##### other| jetbrains
    www.jetbrains.com
    create new account every month?

##### vue| work with axios
    https://github.com/axios/axios
    npm install axios

##### js| promise
"Async и await" https://metanit.com/web/javascript/17.6.php
"Разбираемся с промисами в JavaScript
" https://habr.com/ru/post/439746/

##### js| создание функции для промиса с аргументами
"How to pass parameter to a promise function" https://stackoverflow.com/questions/35318442/how-to-pass-parameter-to-a-promise-function

    var some_function = function (username, password) {
        return new Promise(function (resolve, reject) {
            /* stuff using username, password */
    
            if (/* everything turned out fine */) {
                resolve("Stuff worked!");
            } 
            else {
                reject(Error("It broke"));
            }
        });
    };

##### vue| правильная обрабокта axios
"Обработка ошибок API в веб-приложении, используя Axios" https://medium.com/nuances-of-programming/обработка-ошибок-api-в-веб-приложении-используя-axios-932e9d66a526

    axios.post(url, data)
        .then(res => {
            // do good things
            })
        .catch(err => {
            if (err.response) {
                // client received an error response (5xx, 4xx)
            } 
            else if (err.request) {
                // client never received a response, or request never left
            } 
            else {
                // anything else
            }
    })

##### js| fetch
    try {
        const response = await fetch("api/fruit/all",{method:"GET"});
        const data = await response.json();
        return data;
    } 
    catch (error) {
        return error;
    }


##### vue| на сервере используем
"Error While Importing Axios: Uncaught SyntaxError: Cannot use import statement outside a module
" https://stackoverflow.com/questions/65950850/error-while-importing-axios-uncaught-syntaxerror-cannot-use-import-statement-o
    
    на сервере
    const axios = require('axios');
    на фронет
    import axios from 'axios'

##### js| http-server
"http-server: a simple static HTTP server
" https://www.npmjs.com/package/http-server
"How to install and use Node.js http-server (Web server) via NPM
" https://www.how2shout.com/how-to/how-to-install-and-use-node-js-http-server-web-server-via-npm.html

    npm install http-server
    # name of file index.html
    # in package.json add
    "scripts": {
        ...
        "dev": "http-server -p 8082"
    },

##### other| касперский хак
https://reg.secureitcup.com/todo

##### vue| push in vue
"TypeError: this.$route.push is not a function vue.js and Uncaught TypeError: Cannot read property 'push' of undefined
" https://stackoverflow.com/questions/53340049/typeerror-this-route-push-is-not-a-function-vue-js-and-uncaught-typeerror-can

##### django| get query param by django
"How to access get request data in django rest framework" https://stackoverflow.com/questions/58207014/how-to-access-get-request-data-in-django-rest-framework
test_data_var = request.query_params['testData']

##### vue| create vuex
https://www.youtube.com/watch?v=TQ69S8h1VVU
https://github.com/qirolab/learn-vuex-with-basic-ecommerce-example

##### js| аргументы для функций именованные
"Руководство по JavaScript, часть 4: функции" https://habr.com/ru/company/ruvds/blog/430382/


# Курсы 

##### // node.js
https://github.com/YauhenKavalchuk/node-js

##### // инструкция для npm
https://habr.com/ru/post/133363/#npm_understand

# Видео

##### Require vs Import Javascript
https://www.youtube.com/watch?v=mK54Cn4ceac

# Статьи
mHealth — «мобильное» здравоохранение в современном мире

https://habr.com/ru/company/medgadgets/blog/227159/

Классификация мобильных медицинских приложений, принципы и этические стандарты для их имплементации в клиническую практику

https://medicine-group.ru/classification-medical-app

##### django-cors-headers
    # django-cors-headers 3.13.0

    # забываю
    INSTALLED_APPS = [
        ...,
        "corsheaders",
        ...,
    ]

    CORS_ALLOW_ALL_ORIGINS (old name CORS_ORIGIN_ALLOW_ALL)
    CORS_ALLOWED_ORIGINS (old name CORS_ORIGIN_WHITELIST)

# Django

##### CORS для чайников: история возникновения, как устроен и оптимальные методы работы
https://habr.com/ru/company/macloud/blog/553826/

##### Деплоим изоморфное веб-приложение на примере Nuxt.js
https://habr.com/ru/post/438862/

##### КАК ПОЛЬЗОВАТЬСЯ CURL
https://losst.pro/kak-polzovatsya-curl

###### How to use environment variables in docker-compose?
https://stackoverflow.com/questions/29377853/how-to-use-environment-variables-in-docker-compose

##### Docker container set up for Django & VueJS (well img)
https://stackoverflow.com/questions/53345283/docker-container-set-up-for-django-vuejs

##### Как получить доступ из одного докер-контейнера в другой докер-контейнер
https://habr.com/ru/post/554190/
    
    # внутри друого контенера при использовании docker-compose можно достучать до соседа по имени контенера
    # alias in docker compose does not need
    curl -L http://container-name:8000

##### Want to watch - Реализация RESTFul API на Django REST Framework
https://www.youtube.com/watch?v=C6S3dMt1s_M

###### What is the difference between 0.0.0.0, 127.0.0.1 and localhost?
https://stackoverflow.com/questions/20778771/what-is-the-difference-between-0-0-0-0-127-0-0-1-and-localhost

###### django-channels-daphne-nginx
https://github.com/flutistar/django-channels-daphne-nginx

###### our opponents
https://github.com/AlexGeniusMan/Avia-Hack-2022-RealityX

###### How to use Django with Daphne¶
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/daphne/

# ML

##### Обработка изображений с помощью библиотеки Python Pillow
https://habr.com/ru/post/681248/
https://pypi.org/project/daphne/

# Figma
    
###### 10 лучших UI-китов в Figma для вашего проекта
https://vc.ru/design/231202-10-luchshih-ui-kitov-v-figma-dlya-vashego-proekta
    
    # I used "02. Сontra wireframe kit"

######Bootstrap-v4-uikit
https://www.figma.com/file/DVRWerlYXUuDPpw7mNwfJj/Bootstrap-v4-uikit-(Copy)?node-id=0%3A2507
######Mobile Apps – Prototyping Kit
https://www.figma.com/community/file/1129468881607079432
######contra wireframe kit (Community)
https://www.figma.com/file/BUyLucAxgep6HYskxUQd20/contra-wireframe-kit-(Community)?node-id=185%3A3305
######Mobile Apps – Prototyping Kit (Community)
https://www.figma.com/file/FvlS4ZyJURXyaRBs1XjwiC/Mobile-Apps-–-Prototyping-Kit-(Community)?node-id=101%3A306
######Bootstrap-Grid-v5-for-Responsive
https://www.figma.com/file/MeGftN02aQyHqlLXlKEn2c/Bootstrap-Grid-v5-for-Responsive--گرید-بوت-استرپ-ورژن5-برای-طراحی-واکنشگرا-(Community)?node-id=1%3A58
######Royal-Enfield
https://www.figma.com/file/QKMUuVSCjlMDUt3LkLiSECDn/Royal-Enfield?node-id=0%3A1

######My mobile design
https://www.figma.com/file/b7YC4RyNhNOZ977Rbkmt0I/Untitled?node-id=0%3A1
Mirro desc
https://miro.com/app/board/uXjVPJ2sn1k=/

######Мини-курс «Web Design 2. Figma». Урок 5. Прототипирование
https://www.youtube.com/watch?v=DFIJuW47yd4

######what is it?
https://www.behance.net/

###### Верстка мобильного приложения?
https://proto.io/


# курсы
######курс node
https://www.youtube.com/watch?v=ke4Kl8kE2Lc&t=11s

######курс vue
https://www.youtube.com/watch?v=ke4Kl8kE2Lc&t=11s

######курс ES6
https://www.youtube.com/watch?v=XD1MKx7eIuQ


######Веб-сервер на реальном примере. Docker-compose, nginx, mysql, php-fpm, wordpress.
https://www.youtube.com/watch?v=mKdwkV5p1xg

######Интегрируем Docker в приложение Vue.js
https://ru.vuejs.org/v2/cookbook/dockerize-vuejs-app.html

######Сравниваем эффективность Redis, Kafka и RabbitMQ
https://medium.com/nuances-of-programming/сравниваем-эффективность-redis-kafka-и-rabbitmq-fcd363d5d8c
https://www.youtube.com/watch?v=c_mkpVg5rlg&t=1788s

######Архитектура Web Приложений / от простых до высоконагруженных (лего - смотрел)
https://www.youtube.com/watch?v=9mZmc6a0tmM
https://medium.com/storyblocks-engineering/web-architecture-101-a3224e126947

######CI CD наглядные примеры (смотрел)
https://www.youtube.com/watch?v=ANj7qUgzNq4



######Как реализовать загрузку и загрузку файлов с помощью Express?
https://translated.turbopages.org/proxy_u/en-ru.ru.0d152ca5-6361449a-779c826e-74722d776562/https/www.geeksforgeeks.org/how-to-implement-file-uploading-and-downloading-with-express/

######Interactive Shell Using Docker Compose
https://www.baeldung.com/ops/docker-compose-interactive-shell

######Docker Compose aliases
https://docs.docker.com/compose/compose-file/#aliases

######nuxt-example
https://github.com/BenShelton/nuxt-example

######Django - делаем дамп базы данных и восстанавливаем из него с dumpdata и loaddata
https://the-bosha.ru/2016/06/29/django-delaem-damp-bazy-dannykh-i-vosstanavlivaem-iz-nego-s-dumpdata-i-loaddata/
https://zerotobyte.com/how-to-use-django-loaddata-and-dumpdata/

######Обзор: Puppet, Chef, Ansible, Salt
https://habr.com/ru/post/211306/

######Enabling Cors — Django
https://medium.com/django-rest/django-enabling-cors-9d024351e8f2

######Запускаем PostgreSQL в Docker: от простого к сложному
https://habr.com/ru/post/578744/

######Анализ Данных на Python и Pandas
https://www.youtube.com/watch?v=dd3RcafdOQk

######django_bootstrap5
https://django-bootstrap5.readthedocs.io/en/latest/templates.html

######npm install -g @vue/cli

######Бизнес-логика в Django и архитектура Django проектов — на настоящем примере
https://www.youtube.com/watch?v=LPo29ygf0wA

##### удаление в винде
    # in WebStorm в консоли не было разрешений на установку/удаление - пришлось в cmd
    rm .gitignore
    rmdir /s /q .git


## 04-11-22

##### boostrap install
    https://www.youtube.com/watch?v=oZ9zlS5V5WU
    npm install boostrap
    in mian js add
    import 'bootstrap/dist/css/bootstrap.css'
    import 'bootstrap/dist/js/bootstrap.js'



##### работа с фигомй
    https://www.youtube.com/watch?v=MqW6L3Rdfwo
    шифт-2 - приблизить
    N - переключение
    #адаптивность
    https://www.youtube.com/watch?v=_u5VjLH02M4
    левый верзний угол
    растягивание через ctrl
    шифт-N - переключение обратно
    шифт+Г - отлюкчить сетку везде
    https://www.youtube.com/watch?v=MqW6L3Rdfwo
    alt=ctrL=b - удалить компонент
    таб - движение поэлементам ниже
    разломать мастер компненте - сделать копию а потом разломать

##### bootstrap 
    # в колонке а не в px
    offset-3
    # колонки по центру в1
        <div class="row justify-content-center">
            <div class="col-3 bg-success">
    # колонки по центру в2
        <div class="row">
            <div class="col-3 bg-success mx-auto">


##### вертикальая лини через границы
"Как сделать - вертикальную линию" https://html5css.ru/howto/howto_css_vertical_line.php
    border-left: 6px solid green;

##### прибить футер к ннизу
"Лучший способ прижать футер используя flexbox" https://falbar.ru/article/luchshij-sposob-prizhat-futer-ispolzuya-flexbox
"CSS Flexbox #11 Практические примеры использования Flexbox (Practical examples)
" https://www.youtube.com/watch?v=GGiHxIOmPaE&list=PLNkWIWHIRwMG0EUBS8rvTRVNL9IcxcawW&index=12
    parant flex-direction column
    min-heaight: 100hv
    section flex-grow 1

##### Работа с полями auto_now_add и auto_now в Django и timestamp
https://fixmypc.ru/post/ispolzovanie-polei-v-python-django-auto-now-i-auto-now-add-na-primerakh-pri-rabote-s-metkami-vremeni/

        # если не передали файл в запросе
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']

        # проверка формата файла
        try:
            img = Image.open(f)
            img.verify()
        except:
            raise ParseError("Unsupported image type")

        # RequestData.img.save(f.name, f, save=True)
        a = Data(img=f)
        a.save()
        a.create_processed_data()

        # если попутно передали описание
        if request.data.get('description'):
            a.description = request.data.get('description')
            a.save()

##### имя юзера в API а не id
https://stackoverflow.com/questions/14896825/django-showing-username-and-not-id-how


##### css блок по центру - нужно пркоидыввать h-100
https://myrusakov.ru/bootstrap-center-block.html

##### задать радиус скругления
https://www.w3schools.com/css/css3_borders.asp

##### сделать блок кликабельным
https://neolot.com/uroki-i-priemy/kak-sdelat-klikabelnyj-blok
    div {cursor: pointer;}


##### padding and margin
https://developer.mozilla.org/ru/docs/Web/CSS/margin
    /* Применяется ко всем четырём сторонам */
    margin: 1em;
    
    /* по вертикали | по горизонтали */
    margin: 5% auto;
    
    /* сверху | горизонтально | снизу */
    margin: 1em auto 2em;
    
    /* сверху | справа | снизу | слева */
    margin: 2px 1em 0 auto;

##### вертикальая лини через границы
https://html5css.ru/howto/howto_css_vertical_line.php
    border-left: 6px solid green;

##### css| прибить футер к ннизу
"Лучший способ прижать футер используя flexbox" https://falbar.ru/article/luchshij-sposob-prizhat-futer-ispolzuya-flexbox
"CSS Flexbox #11 Практические примеры использования Flexbox (Practical examples)
"https://www.youtube.com/watch?v=GGiHxIOmPaE&list=PLNkWIWHIRwMG0EUBS8rvTRVNL9IcxcawW&index=12
    parant flex-direction column
    min-heaight: 100hv
    section flex-grow 1

##### js| скрыть/показать элементв jquery
"jQuery & CSS - Remove/Add display:none" https://stackoverflow.com/questions/5059596/jquery-css-remove-add-displaynone
    $('.news').hide();
    $('.news').show();
    !!! запросы jquery только после его подключения

##### js/ функция click jquery
https://api.jquery.com/click/
    $( "#target" ).click(function() {
        alert( "Handler for .click() called." );
    });

##### скруглить картинку
    border-radius: 50%;

##### vue| import css in vue.js
    vue.config.js
    configureWebpack: {
    resolve: {extensions: ['', '.js', '.jsx', '.css']},
    component
    <style scoped>
      @import "../assets/css/login.css";
    </style>

##### vue| install jqeru vue.js
    npm install jquery
    import $ from 'jquery'

##### vue| обзятальео использовать document ready in vue.js
    "$( document ).ready()" https://learn.jquery.com/using-jquery-core/document-ready/
    $(function() {
        console.log( "ready!" );
    });


##### other| beget add url to VPS
    add DNS into req.ru
    ns1.beget.com
    ns2.beget.com
    ns1.beget.pro
    ns2.beget.pro
    вкладка Управление записями DNS
    изменить А - запись у домена на IP сервера
    www.win-plus-ners.ru
    добавить А - запись к домену
    win-plus-ners.ru

##### other| Как поднять домашний сервер со своим доменом своими руками?
https://www.youtube.com/watch?v=avl5rVi-HNo

##### js| как использовать mongo
https://www.youtube.com/watch?time_continue=2&v=LNvmI8a9jwY&feature=emb_logo

##### vue| установить параметры запроса
"How to set URL query params in Vue with Vue-Router" https://stackoverflow.com/questions/40382388/how-to-set-url-query-params-in-vue-with-vue-router
    routes: [
        { name: 'user-view', path: '/user/:id', component: UserView },
        // other routes
        ]
    this.$router.replace({ name: "user-view", params: {id:"123"}, query: {q1: "q1"} })
    this.$router.replace({path: "/user/123", query:{q1: "q1"}})
    this.$route.params.id
    this.$route.query.q1

##### vue| достатьи параметры запроса
"routing with params in vuejs using router-link" https://stackoverflow.com/questions/45734357/routing-with-params-in-vuejs-using-router-link
    <router-link :to="{ name: 'user', params: { userId: 123 }}">User</router-link>

##### vue| работае с датами
"Module not found: Can't resolve 'moment' in 'node_modules\react-moment\dist' in reactjs" https://stackoverflow.com/questions/63137095/module-not-found-cant-resolve-moment-in-node-modules-react-moment-dist-in
    npm i moment
    import moment from 'moment'
    moment(this.date).format'MM/DD/YYYY hh:mm A'


##### vue| ошбка! чтоб страница обновлялассь на
нужно поставить водчер на изменение параметров страницы
    watch: {
        "$route.params.id": {
            handler() {
            this.getImg({id:this.id});
            }
        },
    },

##### vue| модальное окно во vue - плохое - перекрывает стили бутстрап
"Создание модального компонента с помощью Vue.js
" https://habr.com/ru/post/349306/

##### vue| ссылки в виде div
"Vue.js 2.0 router link in a div component" https://stackoverflow.com/questions/41168307/vue-js-2-0-router-link-in-a-div-component
    <router-link to="/about" custom v-slot="{ navigate }">
      <div role="link" @click="navigate">test</div>
    </router-link>

##### vue| несколько ссылок в одном v-on:
"How to call multiple functions with @click in vue?" https://stackoverflow.com/questions/38744932/how-to-call-multiple-functions-with-click-in-vue
    <div @click="firstFunction(); secondFunction();"></div>

##### vue| кнопка добавления в правом верхнем углу элементов уровня блока
"adding button to top right of block level elements" https://stackoverflow.com/questions/6721063/adding-button-to-top-right-of-block-level-elements
    div {
        position: relative;
    }
    div button {
        position: absolute;
        top: 0;
        right: 0;
    }

##### vue| Display different Vuejs components for mobile browsers v1
https://stackoverflow.com/questions/48515023/display-different-vuejs-components-for-mobile-browsers
    <div v-if="!isMobile()">
      <desktop>
      </desktop>
    </div>
    <div v-else>
      <mobile>
      </mobile>
    </div>
    methods: {
     isMobile() {
       if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
         return true
       } else {
         return false
       }
     }
    }

##### vue| Display different Vuejs components for mobile browsers v2
https://stackoverflow.com/questions/48515023/display-different-vuejs-components-for-mobile-browsers
    <production-list v-if="!isMobile()"></production-list>
    <production-list-mobile v-else></production-list-mobile>


##### vue| Как отслеживать ширину экрана Vue? v3
https://qna.habr.com/q/625094
    data: () => ({
    width: 0,
        ...
    }),
    methods: {
        updateWidth() {
            this.width = window.innerWidth;
        },
        ...
        },
    created() {
        window.addEventListener('resize', this.updateWidth);
    },

[//]: # (TODO)
# повторение НА 
CSS Flexbox #11 Практические примеры использования Flexbox (Practical examples)
