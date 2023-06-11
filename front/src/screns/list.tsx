import { Card } from "shoppa-ui/widgets/card";
import { Badge } from "shoppa-ui/widgets/badge";
import { Form } from "shoppa-ui/primitives/form";
import { Input } from "shoppa-ui/widgets/input";
import { Radio } from "shoppa-ui/widgets/radio";
import { Button } from "shoppa-ui/widgets/button";
import { useState, useEffect } from "react";
import { IconButton } from "shoppa-ui/widgets/icon-button";
import { Popup } from "shoppa-ui/primitives/popup";
import { Dialog } from "shoppa-ui/widgets/dialog";
import { API } from "../api";

export type Question = {
  title: string;
  writer: string;
  forWhom: "both" | "omer" | "maya";
};

export const ListScreen = () => {
  const [showPopup, setShowPopup] = useState(false);
  const [showDelPopup, setDelPopup] = useState<false | string>(false);

  const [forWhom, setForWhom] = useState("both");
  const [question, setQuestion] = useState("");
  
  const [myQuestions, setMyQuestions] = useState<Question[]>([]);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    try {
      await API.post("/questions", { text: question, forWhom });
    } catch {
      alert("Failed to add question");
      return;
    }

    setShowPopup(false);
  };

  useEffect(() => {
    (async () => {})();
  }, []);

  return (
    <>
      <Dialog
        show={!!showDelPopup}
        isDanger
        onHide={() => setDelPopup(false)}
        onCancel={() => setDelPopup(false)}
        text="האם בטוח למחוק את השאלה?"
      />
      <Popup
        show={showPopup}
        onHide={() => {
          setShowPopup(false);
        }}
        outerCloseBtn
        className="popup"
      >
        <Form className="d-flex gap-10 flex-column" onSubmit={handleSubmit}>
          <Input
            label="שאלה"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <Radio
            label="לשנינו"
            name="forWho"
            value="both"
            onChange={(e) => setForWhom(e.target.value)}
            defaultChecked
          />
          <Radio
            label="עומר"
            name="forWho"
            value="omer"
            onChange={(e) => setForWhom(e.target.value)}
          />
          <Radio
            label="מאיה"
            name="forWho"
            value="maya"
            onChange={(e) => setForWhom(e.target.value)}
          />
          <Button>הוסף</Button>
        </Form>
      </Popup>
      <div className="d-flex py-20">
        <IconButton label="plus" onClick={() => setShowPopup(true)}>
          <svg
            stroke="currentColor"
            fill="currentColor"
            strokeWidth="0"
            viewBox="0 0 16 16"
            height="1em"
            width="1em"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"></path>
          </svg>
        </IconButton>
      </div>
      <div className="d-flex flex-wrap align-items-stretch gap-20 py-30">
        <Card className="d-flex flex-start flex-column">
          <div className="d-flex flex-start gap-10">
            <Badge title={"אישי"} size="sm" variant="danger" />
            <IconButton
              size="sm"
              variant="link"
              label="trash"
              onClick={() => setDelPopup("popup_id")}
            >
              <svg
                stroke="currentColor"
                fill="currentColor"
                strokeWidth="0"
                viewBox="0 0 24 24"
                height="1em"
                width="1em"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M5 20a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8h2V6h-4V4a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v2H3v2h2zM9 4h6v2H9zM8 8h9v12H7V8z"></path>
                <path d="M9 10h2v8H9zm4 0h2v8h-2z"></path>
              </svg>
            </IconButton>
          </div>
          <h2>מה הדבר הכי יקר שקנית בשנה האחרונה</h2>
        </Card>
        <Card className="d-flex flex-start flex-column">
          <Badge title={"אישי"} size="sm" variant="danger" />
          <h2>מה הדבר הכי יקר שקנית בשנה האחרונה</h2>
        </Card>
        <Card className="d-flex flex-start flex-column">
          <Badge title={"אישי"} size="sm" variant="danger" />
          <h2>מה הדבר הכי יקר שקנית בשנה האחרונה</h2>
        </Card>
      </div>
    </>
  );
};
