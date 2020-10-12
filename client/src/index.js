import axios from 'axios'


const api = (async () => {

    const response =  await axios.get("/api")
    return response.data
  
})().then(res=>{
    populate_sidebar(res)
    populate_articles(res)

})



const populate_sidebar = (data)=> {
    const sidebar = document.querySelector(".sidebar")

    Object.keys(data).forEach(key=>{
   
    const button = create_publication_button(data, key)
    const li = create_publication_li(button)
    sidebar.appendChild(li)
       
    })
}


const create_publication_li = (ele)=>{
    const li = document.createElement('li')
    li.appendChild(ele)
    return li
}

const create_icon = (key) =>{
    const icons = {
        baffler:   "https://thebaffler.com/favicon.ico",
        truthout:   "https://truthout.org/webicons/favicon.ico",
        roarmag: "https://roarmag.org/wp-content/themes/roar-theme/images/favicons/favicon-32x32.png", 
        jacobin:  "https://jacobinmag.com/static/img/logo/logo-favicon.png",
        viewpoint: "https://viewpointmag.com/wp-content/themes/path-child/favicon.ico"
    }

       const icon = document.createElement('img')
       icon.setAttribute("src", icons[key] )

       return icon

}

const create_publication_button = (data, key)=>{
    const button = document.createElement('button')
    const icon = create_icon(key)
    const title = create_publication_title(key)
    button.appendChild(icon)
    button.appendChild(title)

        
    button.addEventListener("click", ()=>{
        empty_articles()
        populate_articles(data, key)
    })
    return button
}

const create_publication_title = (key)=>{
    const title = document.createElement('h4')
    title.innerHTML = key
    return title
}

const populate_articles = (data, publication = Object.keys(data)[0])=>{
    const list = document.querySelector(".articles")

    Object.keys(data).filter(key=> key==publication).forEach(key=>{
        data[publication]["articles"].forEach(article=>{
            const card = create_card(article)
            list.appendChild(card)
        })
    })
}

const create_card = (article)=>{
    const card = document.createElement('li')
    const title = create_title(article.title, article.url)
    const author = create_author(article.author)
    const date = create_date(article.date)
    const metaDataContainer = create_metaDataContainer([author, date])
    card.appendChild(title)
    card.appendChild(metaDataContainer)
    return card


}

const create_title = (str, url) => {
    const title = document.createElement('h2')
    const link = create_link(url) 
    link.innerHTML = str
    title.appendChild(link)

    return title

}

const create_date = (str) => {
    const date = document.createElement('span')
    date.innerHTML = str
    return date
}

const create_author = (str) =>{
    const author = document.createElement('span')
    author.innerHTML = str
    return author
    
}

const create_link = (str)=>{
    const link = document.createElement('a')
    link.setAttribute('href', str)
    return link
}

const create_metaDataContainer = (arr) =>{
    const metaDataContainer = document.createElement('div')
    arr.forEach(element => {
        metaDataContainer.appendChild(element)
    });
    return metaDataContainer
}

const empty_articles = ()=>{
    document.querySelector(".articles").innerHTML = ""

}
