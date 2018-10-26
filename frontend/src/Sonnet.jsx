import React from "react";
import { Paper } from "@material-ui/core";

export function Sonnet({ lines }) {
  return (
    <Paper
      style={{
        width: "100vw",
        height: "content",
        margin: "10px",
        padding: "10px",
        height: "272px"
      }}
    >
      {lines.map((line, key) => (
        <div key={key}>{line}</div>
      ))}
    </Paper>
  );
}
