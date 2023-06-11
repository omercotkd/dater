import { Card } from "shoppa-ui/widgets/card";
import { Form } from "shoppa-ui/primitives/form";
import { Input } from "shoppa-ui/widgets/input";
import { Button } from "shoppa-ui/widgets/button";
import { useState } from "react";
import { API } from "../api";

export const LoginScreen = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    try {
      await API.post("/login", { username, password });
    } catch {
      alert("Login Failed");
      return;
    }

    window.location.reload();
  };

  return (
    <div className="p-50">
      <Form onSubmit={handleSubmit}>
        <Card className=" d-flex flex-column gap-20">
          <h1>Login</h1>
          <Input
            label="Username"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <Input
            label="Password"
            placeholder="Password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button>Login</Button>
        </Card>
      </Form>
    </div>
  );
};
