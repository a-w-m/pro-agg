import populate_articles from "./articles.js";
import populate_sidebar from "./sidebar.js";
import "./style/styles.css";

(async () => {
	const response = await fetch("/api");
	const json = await response.json();
	return json;
})().then((res) => {
	populate_sidebar(res);
	populate_articles(res);
});
