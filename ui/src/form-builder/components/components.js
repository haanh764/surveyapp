export const basicComponents = [
  {
    type: "input",
    label: "Short open answer",
    question: "",
    description: "",
    options: {
      defaultValue: "",
      placeholder: "",
      type: "text"
    }
  },
  {
    type: "input",
    label: "Long open answer",
    question: "",
    description: "",
    options: {
      defaultValue: "",
      placeholder: "",
      type: "textarea"
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
          value: "Option 1",
          text: "Option 1"
        },
        {
          value: "Option 2",
          text: "Option 2"
        },
        {
          value: "Option 3",
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
          value: "Option 1",
          text: "option 1"
        },
        {
          value: "Option 2",
          text: "option 2"
        },
        {
          value: "Option 3",
          text: "option 3"
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
