import React, { useEffect, useState } from "react";
import { Avatar, ButtonGroup, Panel, Button, Navbar, Nav } from "rsuite";
import FRIENDS from "./Friends";
import AUTHORPOSTS from "./AuthorPosts";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import ADD_FRIEND_MODAL from "../Modals/AddFriendModal";
import { getCsrfToken } from "../utils/auth";

function PROFILE() {
	const [posts, setPosts] = React.useState(true);
	const [appearance, setAppearance] = React.useState({
		posts: "primary",
		friends: "ghost",
	});
	const [author, setAuthor] = useState({});
	let navigate = useNavigate();
	const [open, setOpen] = useState(false);

	useEffect(() => {
		if (!localStorage.getItem("loggedIn")) {
			navigate("/login");
		} else {
			setAuthor(localStorage.getItem("user"));
		}
	}, []);

	const handlePostsBtnClick = () => {
		setPosts(true);
		setAppearance({ posts: "primary", friends: "ghost" });
	};

	const handleFriendsBtnClick = () => {
		setPosts(false);
		setAppearance({ posts: "ghost", friends: "primary" });
	};

	const [curPage, setCurPage] = useState("profile");

	const handleInboxClick = () => {
		navigate("/");
	};

	async function handleLogoutClick() {
		await getCsrfToken();
		const token = localStorage.getItem("token");

		let reqInstance = axios.create({
			headers: { "X-CSRFToken": token },
		});
		reqInstance.post("accounts/logout/").then((res) => {
			if (res.status === 200) {
				navigate("/login");
			}
		});
	}

	// make a get request to get author and every post the author made and comments on the posts
	// make a get request to get all the friends of an author

	const handleOpen = () => {
		setOpen(true);
	};

	const handleModalClose = () => {
		setOpen(false);
	};

	return (
		<div style={{ padding: "10px", width: "60%", margin: "auto" }}>
			<Navbar>
				<Navbar.Brand>Socially Distrubted</Navbar.Brand>
				<Nav pullRight>
					<Nav.Item onClick={handleLogoutClick}>Logout</Nav.Item>
				</Nav>
				<Nav pullRight>
					<Nav.Item onClick={handleInboxClick}>Inbox</Nav.Item>
				</Nav>
				<Nav pullRight>
					<Nav.Item>Profile</Nav.Item>
				</Nav>
				<Nav pullRight>
					<Nav.Item onClick={handleOpen}>Add Friend</Nav.Item>
				</Nav>
			</Navbar>
			<Panel shaded>
				<Avatar
					style={{ float: "left" }}
					circle
					src="https://avatars.githubusercontent.com/u/12592949"
					size="lg"
				></Avatar>
				<h2 style={{ marginLeft: "10px", float: "left" }}>
					{author["displayName"]}
				</h2>

				<ButtonGroup
					justified
					style={{ paddingTop: "10px", marginBottom: "5px" }}
				>
					<Button
						style={{ textAlign: "center" }}
						appearance={appearance["posts"]}
						onClick={handlePostsBtnClick}
					>
						Posts
					</Button>
					<Button
						style={{ textAlign: "center" }}
						appearance={appearance["friends"]}
						onClick={handleFriendsBtnClick}
					>
						Friends
					</Button>
				</ButtonGroup>
				{posts ? <AUTHORPOSTS /> : <FRIENDS />}
			</Panel>
			<ADD_FRIEND_MODAL open={open} handleClose={handleModalClose} />
		</div>
	);
}

export default PROFILE;
