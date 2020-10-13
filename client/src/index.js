import axios from "axios";
import populate_articles from "./articles.js";
import populate_sidebar from "./sidebar.js";
import "./style/styles.css";

(async () => {
	const response = await axios.get("/api");
	return response.data;
})().then((res) => {
	populate_sidebar(res);
	populate_articles(res);
});
