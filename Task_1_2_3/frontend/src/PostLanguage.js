import React, { useRef } from "react";
// 'http://127.0.0.1:8000/variables_into_new_language_row?name=Georgian&last_update=2022'

const PostLanguage = (props) => {
  const languageref = useRef();
  const post = () => {
    const language = languageref.current.value;
    fetch(
      `http://127.0.0.1:8000/variables_into_new_language_row?name=${language}&last_update=2022`,
      { method: "POST" }
    );
  };
  return (
    <>
      <form>
        <input ref={languageref} type="text" />
        <button onClick={post}>submit language</button>
      </form>
    </>
  );
};

export default PostLanguage;
