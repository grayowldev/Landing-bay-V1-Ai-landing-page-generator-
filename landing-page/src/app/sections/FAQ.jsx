export const FAQ = ({data}) => {
  return (
    <section className="bg-white py-20">
      <div className="container mx-auto text-center">
        <h2 className="text-3xl font-bold mb-12">Frequently Asked Questions</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {data.faqs.map((item, index) => (
            <div key={index} className="border border-gray-300 rounded-lg p-6 shadow-md">
              <h3 className="text-xl font-semibold mb-4">{item.question}</h3>
              <p className="text-gray-700">{item.answer}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};