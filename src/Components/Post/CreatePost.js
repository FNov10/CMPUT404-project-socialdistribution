import React, { useLayoutEffect, useCallback, useState } from "react";
import {
	Input,
	Avatar,
	useToaster,
	Message,
	Dropdown,
	Uploader,
	Button,
	CheckPicker,
	Checkbox,
} from "rsuite";
import { reqInstance } from "../utils/axios";
import "react-toastify/dist/ReactToastify.css";
import { getAuthorId } from "../utils/auth";
import { useNavigate } from "react-router-dom";
import PROFILEIMAGE from "../Profile/ProfileImage";

// This component handles the creating a post
function CREATEPOST({ refresh }) {
	const [post_status, set_post_status] = useState("PUBLIC");
	const [post_type, set_post_type] = useState("text/plain");
	const [unlisted, setUnlisted] = useState(false);
	const [text, setText] = useState("");
	const [title, setTitle] = useState("");
	const [description, setDescription] = useState("");
	const [categories, setCategories] = useState("");
	const [disabled, setDisabled] = useState(true);
	const [markdown, setMarkdown] = useState("");
	const [authors, setAuthors] = useState([]);
	let navigate = useNavigate();
	const toaster = useToaster();
	const [data, setData] = useState([]);

	function handleClick(eventkey) {
		set_post_status(eventkey);
		if (eventkey === "PRIVATE") {
			setDisabled(false);
		} else {
			setDisabled(true);
		}
	}

	useLayoutEffect(() => {
		if (!localStorage.getItem("loggedIn")) {
			navigate("/signin");
		} else {
			const AUTHOR_ID = getAuthorId(null);
			const url = `authors/${AUTHOR_ID}/followers`;
			reqInstance({
				method: "get",
				url: url,
			}).then((res) => {
				setData(
					res.data.items.map((item) => ({
						label: item["displayName"],
						value: getAuthorId(item["id"]),
					}))
				);
			});
		}
	}, []);

	// this sets input area depending on the type of a post selected by the user
	const input = () => {
		if (post_type === "text/plain") {
			return (
				<div>
					<Input
						style={{
							float: "left",
							marginTop: "5px",
							marginBottom: "5px",
						}}
						as="textarea"
						rows={5}
						placeholder="Text"
						value={text}
						onChange={(e) => setText(e)}
					/>
				</div>
			);
		}

		if (post_type === "text/markdown") {
			return (
				<div>
					<Input
						style={{
							float: "left",
							marginTop: "5px",
							marginBottom: "5px",
						}}
						as="textarea"
						rows={5}
						placeholder="Text"
						value={text}
						onChange={(e) => setText(e)}
					/>
				</div>
			);
		}
		if (post_type === "image/png" || post_type === "image/jpeg") {
			return (
				<div>
					<input id="file" type="file" accept=".png, .jpg, .jpeg" />
				</div>
			);
		}
	};

	const notifySuccessPost = () => {
		toaster.push(<Message type="success">Successful post</Message>, {
			placement: "topEnd",
			duration: 5000,
		});
	};

	const notifyFailedPost = (error) => {
		toaster.push(<Message type="error">{error}</Message>, {
			placement: "topEnd",
			duration: 5000,
		});
	};

	// convertes image into a base64 string
	const toBase64 = (file) =>
		new Promise((resolve, reject) => {
			const reader = new FileReader();
			reader.readAsDataURL(file);
			reader.onload = () => resolve(reader.result);
			reader.onerror = (error) => reject(error);
		});

	// this fucntion handles the Posting of a function
	async function handlePostClick() {
		const author = JSON.parse(localStorage.getItem("user"));
		const author_id = getAuthorId(null);
		const url = `authors/${author_id}/posts/`;

		var params = {
			title: title,
			description: description,
			content: text,
			contentType: post_type,
			visibility: post_status,
			unlisted: unlisted,
			authors: [],
		};

		if (post_status === "PRIVATE") {
			params["authors"] = authors;
		}

		if (post_type === "image/png" || post_type === "image/jpeg") {
			const imagefile = document.getElementById("file").files[0];
			if (imagefile) {
				params["image"] = await toBase64(imagefile);
			}
		}

		if (categories.length > 0) {
			params["categories"] = categories;
		}

		reqInstance({ method: "post", url: url, data: params })
			.then((res) => {
				if (res.status === 200) {
					setText("");
					setDescription("");
					setTitle("");
					setCategories("");
					set_post_status("PUBLIC");
					set_post_type("text/plain");
					setUnlisted(false);
					setMarkdown("");
					setAuthors([]);
					setDisabled(true);
					window.location.reload();
					notifySuccessPost();
				} else {
					notifyFailedPost(res.data);
				}
			})
			.catch((err) => console.log(err));
	}

	return (
		<div
			style={{
				marginBottom: "5px",
				height: "auto",
				border: "1px solid black",
				borderRadius: "10px",
				padding: "5px",
				position: "relative",
			}}
		>
			<PROFILEIMAGE size="md" />
			<Dropdown
				title={post_status}
				activeKey={post_status}
				onSelect={(eventkey) => handleClick(eventkey)}
				style={{ float: "left", marginLeft: "10px" }}
			>
				<Dropdown.Item eventKey="PUBLIC">Public</Dropdown.Item>
				<Dropdown.Item eventKey="FRIENDS">Friends</Dropdown.Item>
				<Dropdown.Item eventKey="PRIVATE">Private</Dropdown.Item>
			</Dropdown>
			<Checkbox onChange={(e) => setUnlisted(true)}>Unlisted</Checkbox>
			<Dropdown
				title={post_type}
				activeKey={post_type}
				onSelect={(eventkey) => set_post_type(eventkey)}
				style={{ float: "left", marginLeft: "10px" }}
			>
				<Dropdown.Item eventKey="text/plain">Plain</Dropdown.Item>
				<Dropdown.Item eventKey="text/markdown">Markdown</Dropdown.Item>
				<Dropdown.Item eventKey="image/png">Png</Dropdown.Item>
				<Dropdown.Item eventKey="image/jpeg">Jpeg</Dropdown.Item>
			</Dropdown>

			<>
				<CheckPicker
					style={{
						float: "left",
						marginLeft: "10px",
						width: 224,
					}}
					label="Friends"
					data={data}
					disabled={disabled}
					valeu={authors}
					onChange={(e) => {
						setAuthors(e);
					}}
				/>
			</>

			<Input
				style={{ float: "left", marginTop: "5px" }}
				as="textarea"
				rows={1}
				placeholder="Categories"
				value={categories}
				onChange={(e) => setCategories(e)}
			/>
			<Input
				style={{ float: "left", marginTop: "5px" }}
				as="textarea"
				rows={1}
				placeholder="Title"
				value={title}
				onChange={(e) => setTitle(e)}
			/>
			<Input
				style={{ float: "left", marginTop: "5px" }}
				as="textarea"
				rows={1}
				placeholder="description"
				value={description}
				onChange={(e) => setDescription(e)}
			/>
			{input()}
			<Button
				style={{ marginTop: "3px" }}
				onClick={handlePostClick}
				appearance="primary"
				block
			>
				Post
			</Button>
		</div>
	);
}

export default CREATEPOST;
