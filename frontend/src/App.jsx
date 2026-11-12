import { BrowserRouter, Route, Routes } from 'react-router-dom'

function Home() {
  return <main><h1>AskMyDocs</h1><p>Project foundation is ready.</p></main>
}

export default function App() {
  return <BrowserRouter><Routes><Route path="/" element={<Home />} /></Routes></BrowserRouter>
}
