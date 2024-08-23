'use client'
export const Hero = ({data}) => {
  return (
    <section className="bg-gray-100 py-80">
      <div className="container mx-auto text-center">
        <h1 className="text-4xl font-bold mb-4">{data.heading}</h1>
        <p className="text-lg mb-8">
          {data.subheading}
        </p>
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Learn More
        </button>
      </div>
    </section>
  );
};
