export const Pricing = () => {
  return (
    <section className="bg-white py-20">
      <div className="container mx-auto text-center">
        <h2 className="text-3xl font-bold mb-12">Pricing Plans</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="border border-gray-300 rounded-lg p-8 shadow-md">
            <h3 className="text-xl font-semibold mb-4">Basic</h3>
            <p className="text-4xl font-bold mb-6">$19/mo</p>
            <ul className="text-gray-700 mb-8">
              <li className="mb-2">Feature 1</li>
              <li className="mb-2">Feature 2</li>
              <li>Limited Support</li>
            </ul>
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              Get Started
            </button>
          </div>
          <div className="border border-gray-300 rounded-lg p-8 shadow-md">
            <h3 className="text-xl font-semibold mb-4">Pro</h3>
            <p className="text-4xl font-bold mb-6">$49/mo</p>
            <ul className="text-gray-700 mb-8">
              <li className="mb-2">All Basic Features</li>
              <li className="mb-2">Feature 3</li>
              <li>Priority Support</li>
            </ul>
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              Get Started
            </button>
          </div>
          <div className="border border-gray-300 rounded-lg p-8 shadow-md">
            <h3 className="text-xl font-semibold mb-4">Enterprise</h3>
            <p className="text-4xl font-bold mb-6">Contact Us</p>
            <ul className="text-gray-700 mb-8">
              <li className="mb-2">All Pro Features</li>
              <li className="mb-2">Custom Integrations</li>
              <li>Dedicated Support</li>
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