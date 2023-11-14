import Image from 'next/image'
import Clock from './components/clock'
import Counter from './components/Counter'
import Comp from './components/Comp'

export default function Home() {
  return (
    <div> 
      <Clock />
      <Counter />
      <Comp />
    </div>
  )
}
