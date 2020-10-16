import "./style/article.css";

const populate_articles = (data, publication = Object.keys(data)[0]) => {
	const list = document.querySelector(".articles");
	const pubs = publication === "all" ? Object.keys(data) : [publication];

	pubs.forEach((key) => {
		data[key]["articles"].forEach((article) => {
			const card = create_article_component(article);
			list.appendChild(card);
		});
	});
};

const create_article_component = (article) => {
	const card = document.createElement("li");
	const title = create_title(article.title, article.url);
	const author = create_author(article.author, article.author_url);
	const date = create_date(article.date);
	const metaDataContainer = create_metaDataContainer([author, date]);
	card.appendChild(title);
	card.appendChild(metaDataContainer);
	return card;
};

const create_title = (str, url) => {
	const title = document.createElement("h2");
	const link = create_link(url);
	link.innerHTML = str;
	title.appendChild(link);

	return title;
};

const create_date = (str) => {
	const date = document.createElement("span");
	date.innerHTML = str;
	return date;
};

const create_author = (str, url) => {
	const link = create_link(url);
	const author = document.createElement("span");
	link.innerHTML = str;
	author.appendChild(link);
	return author;
};

const create_link = (str) => {
	const link = document.createElement("a");
	link.setAttribute("href", str);
	return link;
};

const create_metaDataContainer = (arr) => {
	const metaDataContainer = document.createElement("div");
	arr.forEach((element) => {
		metaDataContainer.appendChild(element);
	});
	return metaDataContainer;
};

export default populate_articles;
