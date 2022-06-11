import { DATA_MODEL, FORM_MODEL } from "./constant";

export function genFormItemTemp(widget) {
  let template = `
        <div>
          <h1>
            ${widget.question || "Survey question"}
          </h1>
          <p>
            ${widget.description}
          </p>
        </div>
        <div label="${widget.name}" prop="${widget.model}">
          ${genWidgetTemp(widget, true)}
        </div>
    `;
  return template;
}

function genWidgetTemp(widget, isForm = false) {
  let widgetTemp = "";
  let { options, placeholder } = widget.options;
  const model = `${isForm ? FORM_MODEL : DATA_MODEL}.${widget.model}`;
  if (widget.type === "input") {
    let type = "text";
    widgetTemp += `<v-text-field
          type="${type}"
          v-model="${model}"
          placeholder="${placeholder}"
        ></v-text-field>`;
  } else if (widget.type === "radio") {
    const optionArr = options;
    const optionFunc = () => {
      let optStr = "";
      for (const item of optionArr) {
        optStr += `
        <v-radio
            label="${item.text}"
            value="${item.value}"
            key="${item.value}">
            ${item.label}
          </v-radio>`;
      }
      return optStr;
    };
    widgetTemp += `<v-radio-group
          v-model="${model}"
           >
              ${optionFunc()}
      </v-radio-group>`;
  } else if (widget.type === "checkbox") {
    const optionArr = options;
    const optionFunc = () => {
      let optStr = "";
      for (const item of optionArr) {
        optStr += `
        <v-checkbox
            label="${item.text}"
            v-model="${model}"
            value="${item.value}"
            key="${item.value}">
          </v-checkbox>
          `;
      }
      return optStr;
    };
    widgetTemp += `<v-item-group
          v-model="${model}" >
              ${optionFunc()}
      </v-item-group>`;
  } else if (widget.type === "slider") {
    widgetTemp += `<v-slider
        v-model="${model}"
        :min="${widget.options.min}"
        :max="${widget.options.max}"
        :step="${widget.options.step}"
      />`;
  } else if (widget.type === "text") {
    widgetTemp += `<${widget.options.tag || "span"}>{{${model}}}</${
      widget.options.tag || "span"
    }>`;
  }
  return widgetTemp;
}
