export const Testimonials = ({data}) => {
  return (
    <section className="bg-gray-100 py-20" style={{background: '#EAE9E5'}}>
      <div className="container mx-auto text-center">
        <h2 className="text-3xl font-bold mb-12">{data.title}</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div className="bg-white border border-gray-300 rounded-lg p-8 shadow-md">
            <p className="text-gray-700 mb-4">
              {data.testimonials[0].content}
            </p>
            <p className="font-semibold">- {data.testimonials[0].author}, {data.testimonials[0].company}</p>
          </div>
          <div className="bg-white border border-gray-300 rounded-lg p-8 shadow-md">
            <p className="text-gray-700 mb-4">
              {data.testimonials[1].content}
            </p>
            <p className="font-semibold">- {data.testimonials[1].author}, {data.testimonials[1].company}</p>
          </div>
          <div className="bg-white border border-gray-300 rounded-lg p-8 shadow-md">
            <p className="text-gray-700 mb-4">
              {data.testimonials[2].content}
            </p>
            <p className="font-semibold">- {data.testimonials[1].author}, {data.testimonials[1].company}</p>
          </div>
        </div>
      </div>
    </section>
  );
};