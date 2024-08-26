import Image from "next/image";
import {Header} from "@/app/sections/Header";
import {Hero} from "@/app/sections/Hero";
import Benefits from "@/app/sections/Benefits";
import {Features} from "@/app/sections/Features";
import {Pricing} from "@/app/sections/Pricing";
import {Testimonials} from "@/app/sections/Testimonials";
import {CallToAction} from "@/app/sections/CallAction";
import {FAQ} from "@/app/sections/FAQ";
import {Footer} from "@/app/sections/Footer";

import fs from 'fs';
import path from 'path';



export default function Home() {

  const filePath = path.join(process.cwd(),'src', 'app', 'pageContent.json');
  const jsonData = fs.readFileSync(filePath, 'utf8');
  const data = JSON.parse(jsonData);


  return (
      <div>
          <Hero data={data.hero} ></Hero>
          <Benefits data={data.benefits}></Benefits>
          <Features data={data.features}></Features>
          <Testimonials data={data.testimonials}></Testimonials>
          <Pricing data={data.pricing}></Pricing>
          <CallToAction></CallToAction>
          <FAQ data={data.faq}></FAQ>
          <Footer></Footer>
      </div>
  );
}
