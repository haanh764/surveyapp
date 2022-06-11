import { DATA_MODEL, FORM_MODEL } from "./constant";
import { genFormItemTemp } from "./generateFormItemCode";

let models;
let rules;
let dataModel;

export default function genFormCode(data, value) {
  models = {};
  rules = {};
  dataModel = {};
  const res = generateModel(data.list, value, models, rules);
  Object.assign(models, res.models);
  Object.assign(rules, res.rules);
  Object.assign(dataModel, res.dataModel);

  let templateCode = `<template>
    <div>
      <div
        ref="generateForm"
        :model="${FORM_MODEL}"
        :rules="rules"
      >`;

  for (let widget of data.list) {
    templateCode += genFormItemTemp(widget);
  }

  templateCode += `</div>
    </div>
  </template>`;

  const scriptCode = `<script>
    export default {
      name:'form-builder',
        data() {
          return {
            ${FORM_MODEL}: ${JSON.stringify(models)},
            rules: ${strToRegExp(JSON.stringify(rules))},
            ${DATA_MODEL}: ${JSON.stringify(dataModel)},
          };
        },
        created() {
            console.log("***SUCCESS***");
        },
        methods: {}
    }
    </script>`;
  const styleCode = "";
  const result = templateCode + "\r\n" + scriptCode + "\r\n" + styleCode;
  console.log(result);
  return result;
}

function strToRegExp(str) {
  const reg1 = /("pattern":)(.*?)((",)|(" ,))/g;
  const reg2 = /"([^"]*)"/g;
  let result = str,
    regArr1,
    regArr2;
  regArr1 = str.match(reg1);
  if (!regArr1) return result;
  regArr2 = regArr1.map((b) => decodeURI(b.replace(reg2, "$1")));
  regArr1.map((b, index) => {
    if (str.indexOf(b) !== -1) {
      result = result.replace(b, regArr2[index]);
    }
  });
  return result;
}

function generateModel(genList, value) {
  for (let i = 0; i < genList.length; i++) {
    if (genList[i].type === "grid") {
      genList[i].columns.forEach((item) => {
        generateModel(item.list);
      });
    } else {
      if (value && Object.keys(value).indexOf(genList[i].model) >= 0) {
        models[genList[i].model] = value[genList[i].model];
      } else {
        models[genList[i].model] = genList[i].options.defaultValue;
      }

      dataModel[genList[i].model] = models[genList[i].model];

      if (rules[genList[i].model]) {
        rules[genList[i].model] = [
          ...rules[genList[i].model],
          ...(genList[i].rules || []).map((item) => {
            if (item.pattern) {
              return { ...item, pattern: encodeURI(item.pattern) };
            } else {
              return { ...item };
            }
          })
        ];
      } else {
        rules[genList[i].model] = [
          ...(genList[i].rules || []).map((item) => {
            if (item.pattern) {
              return { ...item, pattern: encodeURI(item.pattern) };
            } else {
              return { ...item };
            }
          })
        ];
      }
    }
  }
  return { models, rules, dataModel };
}
