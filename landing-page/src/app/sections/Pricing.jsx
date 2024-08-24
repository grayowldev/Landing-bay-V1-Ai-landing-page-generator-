export const Pricing = ({data}) => {
  return (
    <section className="bg-white py-20">
      <div className="container mx-auto text-center">
        <h2 className="text-3xl font-bold mb-12">{data.title}</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="border border-gray-300 rounded-lg p-8 shadow-md">
            <h3 className="text-xl font-semibold mb-4">{data.categories[0].name}</h3>
            <p className="text-4xl font-bold mb-6">{data.categories[0].price}</p>
            <ul className="text-gray-700 mb-8">
              <li className="mb-2">{data.categories[0].features[0]}</li>
              <li className="mb-2">{data.categories[0].features[1]}</li>
              <li>{data.categories[0].features[2]}</li>
            </ul>
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              Get Started
            </button>
          </div>
          <div className="border border-gray-300 rounded-lg p-8 shadow-md">
            <h3 className="text-xl font-semibold mb-4">{data.categories[1].name}</h3>
            <p className="text-4xl font-bold mb-6">{data.categories[1].price}</p>
            <ul className="text-gray-700 mb-8">
              <li className="mb-2">{data.categories[1].features[0]}</li>
              <li className="mb-2">{data.categories[1].features[1]}</li>
              <li>{data.categories[1].features[2]}</li>
            </ul>
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              Get Started
            </button>
          </div>
          <div className="border border-gray-300 rounded-lg p-8 shadow-md">
            <h3 className="text-xl font-semibold mb-4">{data.categories[2].name}</h3>
            <p className="text-4xl font-bold mb-6">{data.categories[2].price}</p>
            <ul className="text-gray-700 mb-8">
              <li className="mb-2">{data.categories[2].features[0]}</li>
              <li className="mb-2">{data.categories[2].features[1]}</li>
              <li>{data.categories[2].features[2]}</li>
            </ul>
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              Contact Sales
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};