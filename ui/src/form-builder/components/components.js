export const basicComponents = [
  {
    type: "input",
    label: "Open answer",
    question: "",
    description: "",
    options: {
      defaultValue: "",
      placeholder: ""
    }
  },
  {
    type: "radio",
    label: "Single choice",
    question: "",
    description: "",
    options: {
      defaultValue: "",
      options: [
        {
          value: "Option_1",
          text: "Option 1"
        },
        {
          value: "Option_2",
          text: "Option 2"
        },
        {
          value: "Option_3",
          text: "Option 3"
        }
      ]
    }
  },
  {
    type: "checkbox",
    label: "Multiple choices",
    question: "",
    description: "",
    options: {
      defaultValue: [],
      options: [
        {
          value: "Option_1",
          text: "Option 1"
        },
        {
          value: "Option_2",
          text: "Option 2"
        },
        {
          value: "Option_3",
          text: "Option 3"
        }
      ]
    }
  },
  {
    type: "slider",
    label: "Slider",
    question: "",
    description: "",
    options: {
      defaultValue: 0,
      min: 0,
      max: 100,
      step: 1
    }
  },
  {
    type: "text",
    label: "Headings",
    options: {
      tag: "h1",
      defaultValue: "This is a heading"
    }
  },
  {
    type: "text",
    label: "Paragraph",
    options: {
      tag: "p",
      defaultValue: "This is a text"
    }
  }
];
