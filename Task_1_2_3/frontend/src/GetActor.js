import React, { useState, useEffect } from "react";

const GetActor = (props) => {
  const [actors, setActors] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/actor_by_film?first_letter=D")
      .then((response) => response.json())
      .then((json) => {
        console.log(json);
        setActors(json);
      });
  }, []);
  return (
    <>
      <ul>
        {actors.map((actor_by_film) => (
          <li key={actor_by_film}>
            Actor name {actor_by_film[0]} {actor_by_film[1]} Films{" "}
            {actor_by_film[2]}
          </li>
        ))}
      </ul>
    </>
  );
};
export default GetActor;

// import React, { useState, useRef, useEffect } from "react";
