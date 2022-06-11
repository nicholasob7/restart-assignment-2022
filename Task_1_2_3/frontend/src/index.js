import React from "react";
import ReactDOM from "react-dom/client";
import GetActor from "./GetActor";
import PostLanguage from "./PostLanguage";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <>
    <GetActor>get_actor_by_film</GetActor>

    <PostLanguage>insert_variables_into_new_language_row</PostLanguage>
  </>
);
