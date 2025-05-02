Title: Demo Driven Development: Show, Don't Just Tell
Date: 2025-05-02 10:20
Category: posts
Tags: software
Slug: demo-driven-development
Authors: Shubhanshu Mishra
Summary: Demo Driven Development

In the whirlwind world of software development, especially when navigating uncharted territories and rapid iterations, how do we ensure we're building the right thing? For too long, the default has been to meticulously craft Product Requirements Documents (PRDs) or Requests for Comments (RFCs) before even a single line of code is written. But what if there's a more dynamic and insightful approach? Enter **Demo Driven Development**.

The core idea is simple yet powerful: in environments marked by speed and significant uncertainty, prioritizing the creation of tangible **demos** over exhaustive documentation can be a game-changer. Instead of pages of text describing a vision, a working (albeit potentially rough) demo allows for immediate interaction and feedback from users and stakeholders.

Think about it – which is more impactful: reading a lengthy document explaining a new feature, or actually clicking through a basic interface and experiencing it firsthand?

### What Exactly is a Demo?

Let's break down the essence of a demo in this context:

1.  **It has an interface you can touch:** Unlike a static document, a demo provides a tangible surface for stakeholders to interact with. This could be a web page, a basic mobile app screen, or even a command-line interface.
2.  **A Living Vision:** While well-crafted PRDs and RFCs are crucial for outlining the thought process and long-term vision, a demo breathes life into that vision. It's the scrappy prototype that makes abstract ideas concrete.
3.  **Experience Over Explanation:** The focus is on *showing* and allowing users to *experience* the core functionality, rather than simply telling them about it. Hand someone a demo and let them explore; the insights gained will often surpass those gleaned from reading a document.
4.  **Not the Final Product (Yet!):** It's vital to remember that a demo is not the polished, production-ready application. Its primary purpose is to demonstrate key concepts and gather feedback. Accessibility is key to ensure everyone can engage, but initial usability can take a backseat to getting the core idea across. Once feedback starts flowing, then the focus can shift towards refining the user experience.
5.  **Small Team, Big Impact:** Ideally, a single person or a very small team should own the creation of a demo. It shouldn't require a massive effort, as it's a means to an end – understanding and validation – not the end itself.

### How Teams Can Embrace Demo Driven Development

Shifting towards a demo-centric approach requires a conscious effort and the right mindset:

1.  **Empower Demo Creation:** Make it easy for developers to build demos. This means providing the right tools, libraries, and encouraging them to prioritize a working prototype over extensive upfront documentation.
2.  **Simplify Demo Access:** Lower the barrier to entry for stakeholders to interact with demos. This could involve easy-to-set-up web endpoints, readily deployable mobile app demos (think Expo for React Native), or simple installation scripts.
3.  **Integrate Demos into the Workflow:** Make demos a natural part of the development process. This could involve regular demo sessions, incorporating demos into feedback loops, and using demos as a basis for discussion and decision-making.
4.  **Focus Feedback, Not Flaws:** Encourage stakeholders to focus their feedback on the core concepts being demonstrated, rather than nitpicking minor UI inconsistencies or non-essential details. The onus is on those providing feedback to see past the rough edges.
5.  **Invest in Prototyping Tools:** Consider investing in tooling that allows for rapid prototyping that closely resembles the actual product surfaces. This can help bridge the gap between the initial demo and the final product.

### When Docs Still Reign Supreme

While Demo Driven Development offers significant advantages, documentation still holds a crucial place:

* **From Demo to Direction:** Once a demo gains traction and provides valuable feedback, the individual responsible should then synthesize those learnings and create more formal documentation to articulate the refined requirements and secure buy-in for full product development.
* **Laying the Foundation for Production:** Documentation becomes essential when specifying the intricacies of a production setup, including reliability, performance requirements, and architectural decisions. While a demo showcases the "what," documentation often defines the "how" for a scalable and robust solution.

In conclusion, in the fast-paced and often ambiguous world of modern software development, Demo Driven Development offers a powerful alternative to solely relying on upfront documentation. By prioritizing tangible experiences and rapid feedback loops, teams can navigate uncertainty more effectively, gather diverse perspectives, and ultimately build products that truly resonate with their users. So, let's move beyond just talking about it, and start showing what's possible.

<details>
<summary>Prompt to LLM to generate the first draft of the blog content:</summary>
Format these thoughts into a blogpost style: 

Title: Demo Driven Development

Key Idea: Demo Driven Development in software teams is helpful than PRD driven development (or Doc Driven development) especially in rapid moving field with large uncertainity. Building demos instead of docs allows us to get user and stakeholder feedback rapidly. Also using demos allows us to get more diverse feedback from non developers. Finally, demos allows us to identify key bottlenecks of building things and also allow us to explore possibilities. 

What is a demo:
1. It has an interface which stakeholders can interact.
2. Good PRD/RFCs are like demos but they help explain the thought process and provide a vision. A demo provides life to a vision, although it is scrapy.
3. Focused on Show/Experience rather than tell. If I just give you the demo and help you explore it it will be more illustrative than making you read a doc.
4. Demo is not the final product. Ideally it should help demonstrate the key ideas to the relevant stakeholders. Usability of demo should not be a priority over Accessibility. Once the demo is done and feedback starts flowing, focus on improving usability.
5. A demo should not require a big team to build, ideally one person should be able to take ownership of the demo. A demo is not the product so it should not require a lot of effort.


What can teams do to enable demo driven development:
1. Make demo development easier. Have the right tools, encourage developers to prioritize building a demo rather than writing a doc. 
2. Make demo access easier, e.g. easy to setup a web endpoint to access the demo, easy to try a mobile app for demo (e.g. expo for React Native)
3. Make demos part of the process
4. Discourage nitpicking the demo and avoid discussion on the non essential parts of the demo. This onus is on the people providing feedback
5. Try to allow demos to be as close the the actual product surfaces, invest in tooling around these. 

What are the cases where docs are still important for development. 
- While demos help us get feedback and a general feel of the work, once the demo starts gaining tracking, the individual responsible for the demo should then distill the ideas and generate the buy in for the product development work
- Docs should help specify the learnings and the requirement for production setup where things need to be reliable and performant.

</details>
