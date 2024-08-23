export const Testimonials = () => {
  return (
    <section className="bg-gray-100 py-20">
      <div className="container mx-auto text-center">
        <h2 className="text-3xl font-bold mb-12">What Our Customers Say</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div className="bg-white border border-gray-300 rounded-lg p-8 shadow-md">
            <p className="text-gray-700 mb-4">
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod nisi eget magna aliquam."
            </p>
            <p className="font-semibold">- John Doe, Company X</p>
          </div>
          <div className="bg-white border border-gray-300 rounded-lg p-8 shadow-md">
            <p className="text-gray-700 mb-4">
              "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam."
            </p>
            <p className="font-semibold">- Jane Smith, Company Y</p>
          </div>
          <div className="bg-white border border-gray-300 rounded-lg p-8 shadow-md">
            <p className="text-gray-700 mb-4">
              "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
            </p>
            <p className="font-semibold">- David Lee, Company Z</p>
          </div>
        </div>
      </div>
    </section>
  );
};