import { useEffect } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const coins = async () => {
    await axios
      .get("https://49ca-2401-4900-1c74-29a8-ad11-8d9-775b-192f.in.ngrok.io/", {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((data) => console.log(data))
      .catch((err) => console.log(err.message));
    return;
  };

  useEffect(() => {
    coins();
  }, []);

  return (
    <div>
      <p> Hi</p>
    </div>
  );
}

export default App;
