
import { GoogleGenAI } from "@google/genai";

export async function askGemini(prompt: string, imageBase64?: string) {
  const ai = new GoogleGenAI({ apiKey: process.env.API_KEY || '' });
  try {
    const model = 'gemini-2.5-flash-preview-tts'; // Using a model that supports multi-modal and fast response
    
    let contents: any;
    if (imageBase64) {
      contents = {
        parts: [
          { inlineData: { mimeType: "image/jpeg", data: imageBase64 } },
          { text: prompt || "Please analyze this technical lubrication schedule page and extract equipment details like Tag No, Lubricant Type, and Replacement Interval." }
        ]
      };
    } else {
      contents = prompt;
    }

    const response = await ai.models.generateContent({
      model: 'gemini-3-flash-preview',
      contents: contents,
      config: {
        systemInstruction: `You are a world-class mechanical engineer and lubrication specialist for Petrofac at the Ain Tsila Development in Algeria. 
        The user is providing parts of a Lubrication and Operating Fluid Schedule.
        Your goal is to:
        1. Extract specific data (Tag No, Description, Part, Lubricant Grade, Intervals) if an image is provided.
        2. Answer technical queries in both Arabic and English as requested by the user.
        3. Help technicians find alternative lubricants if the primary brand is out of stock.
        Keep answers professional, technically accurate, and concise.`,
        temperature: 0.5,
      },
    });
    return response.text;
  } catch (error) {
    console.error("Gemini Error:", error);
    return "I'm having trouble connecting to my technical knowledge base. Please check your connection.";
  }
}
