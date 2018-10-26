import React, { Component } from "react";
import { Button, Paper } from "@material-ui/core";
import { Sonnet } from "./Sonnet";
import styled from "styled-components";

const Row = styled.div`
  display: flex;
  flex-direction: row;
  width: 100%;
`;

const Column = styled.div`
  display: flex;
  flex-direction: column;
  height: 100%;
`;

const buildLinesFromWords = words => {
  let lines = [];
  for (let i = 0; i < 14; i++) {
    let line = [];
    for (let j = 0; j < 8; j++) {
      line.push(words.shift());
    }
    lines.push(line.join(" "));
  }

  return lines;
};

const convertJsonToLineArray = i => {
  return json => {
    const joined = json.join(" ");
    const words = joined.replace("\n", " ").split(" ");
    const sliced = words.slice(i);

    return buildLinesFromWords(sliced);
  };
};

const tap = data => {
  console.log(data);
  return data;
};

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      drunk: [],
      sober: [],
      seuss: []
    };
  }

  request = route => {
    const convert = convertJsonToLineArray(Math.random() * 900);
    fetch(`http://localhost:5000/${route}`)
      .then(res => res.json())
      .then(json => {
        return convert(json);
      })
      .then(myJson =>
        this.setState(() => ({
          [route]: myJson
        }))
      );
  };

  render() {
    return (
      <Column>
        <Row>
          <Button
            onClick={() => this.request("sober")}
            style={{ width: "300px" }}
          >
            Let the bard speaketh
          </Button>
          <Sonnet lines={this.state.sober} />
        </Row>
        <Row>
          <Button onClick={() => this.request("drunk")}>
            Pour Shakespear a drink
          </Button>
          <Sonnet lines={this.state.drunk} style={{ width: "300px" }} />
        </Row>
      </Column>
    );
  }
}

export default App;
