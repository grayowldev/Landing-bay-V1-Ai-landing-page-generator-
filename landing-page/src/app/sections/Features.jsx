export const Features = ({data}) => {
  return (
    <section className="bg-gray-100 py-20" style={{background: '#EAE9E5'}}>
      <div className="container mx-auto text-center">
        <h2 className="text-3xl font-bold mb-12">{data.title}</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 className="text-xl font-semibold mb-4">Feature 1</h3>
            <p className="text-gray-700">
              {data.features[0]}
            </p>
          </div>
          <div>
            <h3 className="text-xl font-semibold mb-4">Feature 2</h3>
            <p className="text-gray-700">
              {data.features[1]}
            </p>
          </div>
          <div>
            <h3 className="text-xl font-semibold mb-4">Feature 3</h3>
            <p className="text-gray-700">
              {data.features[2]}
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};