import populate_articles from "./articles";
import "./style/button.css";

const populate_sidebar = (data) => {
	const sidebar = document.querySelector(".sidebar");

	Object.keys(data).concat("all").forEach((key) => {
		if (data[key]!== null){
		const button = create_publication_button(data, key);
		const li = document.createElement("li");
		li.appendChild(button);
		sidebar.appendChild(li);
		}
	});


};


const create_publication_button = (data, key) => {
	const button = document.createElement("button");
	const wrapper = document.createElement("div");
	
	const icon = (key !== "all")? create_icon(key): create_sigma();
	const title = create_publication_title(key);
	if (icon) {wrapper.appendChild(icon);}
	wrapper.appendChild(title);
	button.appendChild(wrapper);

	button.addEventListener("click", () => {
		empty_articles();
		populate_articles(data, key);
	});
	return button;
};

const create_sigma = ()=>{
	const sigma = document.createElement('span')
	return sigma
}

const create_icon = (key) => {
	const icons = {
		baffler: "https://thebaffler.com/favicon.ico",
		truthout: "https://truthout.org/webicons/favicon.ico",
		roarmag:
			"https://roarmag.org/wp-content/themes/roar-theme/images/favicons/favicon-32x32.png",
		jacobin: "https://jacobinmag.com/static/img/logo/logo-favicon.png",
		viewpoint:
			"https://viewpointmag.com/wp-content/themes/path-child/favicon.ico",
	};

	const icon = document.createElement("img");
	icon.setAttribute("src", icons[key]);

	return icon;
};

const create_publication_title = (key) => {
	const title = document.createElement("h4");
	title.innerHTML = key;
	return title;
};

const empty_articles = () => {
	document.querySelector(".articles").innerHTML = "";
};

export default populate_sidebar;
