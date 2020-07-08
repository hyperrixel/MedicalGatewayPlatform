[![Generic badge](https://img.shields.io/badge/Version-v_1.0-001850.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/State-dev_released-ffa000.svg)](https://shields.io/)<br>

# MGP - Medical Gateway Platform

## What is this?

Medical Gateway Platform is a data driven solution to connect medical hardware or equipment and to support real-time secure and private data sharing.

[![MGP - Medical Gateway Platform](https://i.ytimg.com/vi_webp/5xtFjudCny8/maxresdefault.webp)](https://youtu.be/5xtFjudCny8)

## How it works?

Medical Gateway Platform is a large system which involves many use-cases. To have an idea how you could use this system and its advantages first of all you have to read one of the next sections of this part. The concrete section depends on who you are and what your goal is.

![Architecture](https://github.com/hyperrixel/MedicalGatewayPlatform/blob/master/screenshots/architecture.png "Architecture")

The platform has *5* big parts:
- ` input handler ` area
- ` process ` area
- ` gateway ` area
- ` output handler ` area
- ` data storage and storage handler ` area

Dataflow

![Dataflow](https://github.com/hyperrixel/MedicalGatewayPlatform/blob/master/screenshots/dataflow.png "Dataflow")

### Developers of ventilator projects

You can download some of our source from ` source_python `, ` source_java ` or ` source_cpp ` folder to get familiar with the concept of the code.

### Screenshots

#### Main screen

![Main screen](https://github.com/hyperrixel/MedicalGatewayPlatform/blob/master/screenshots/main.png "Main screen")

#### Screen of doctors


Doctors see patient-related data on one dedicated page with the most important features such as name, ventilatory patterns, breathing cycle graph and status bar for signaling okay, warning and alarm statuses. Data are shown on patient-related unique cards. Adding new patient is easy with the giant bubble button. These screens work not only desktop computers, but mobile devices as well. Huge buttons support the functionality during easy clickability to medical staff with gloves.

![Patients](https://github.com/hyperrixel/MedicalGatewayPlatform/blob/master/screenshots/patients.png "Patients") | ![Add new patient](https://github.com/hyperrixel/MedicalGatewayPlatform/blob/master/screenshots/patients_add_new.png "Add new patient")
------------ | -------------

#### Screen of developers

Skeletons of developers’ screens are similar like interface for doctors but filled with different contents. There are multiple way to create new code. First of all there is a chance to load in an already existed open source project. Secondly, developers are able to choose the ventilation workflow only option. It is useful for designing a product or build code based on an empty guideline. Finally, hardcore programmers are able to write a brand new code from sratch. However, these are the main categories, we provide a wizard helping system even if they used a brand new code option. We help to anybody at anytime during the coding process. That’s why we have a lint-alike feedback system. This helps to fix error faster and be patient safe.

![Developer new code](https://github.com/hyperrixel/MedicalGatewayPlatform/blob/master/screenshots/developer_new_code.png "Developer new code") | ![Developer error](https://github.com/hyperrixel/MedicalGatewayPlatform/blob/master/screenshots/developer_error.png "Developer error")
------------ | -------------

#### Screen of administrators

We decided to show a screen about one of our greatest side-invention: oxygen level optimalization. In a hospital where multiple device is used from a built-in oxygen source, devices can load the oxygen network unbalanced. The devices are able to optimize the breathing sequences for balancing the consumption. The process time depends on the number of devices and the type of used breathing sequences.  If a developer adopt this functionality, different devices can be work together to release the most capacity as possible.

![Oxygen optimalization](https://github.com/hyperrixel/MedicalGatewayPlatform/blob/master/screenshots/o2_optimizing.png "Oxygen optimalization") | ![Oxygen optimalization auto](https://github.com/hyperrixel/MedicalGatewayPlatform/blob/master/screenshots/o2_optimizing_tooltip.png "Oxygen optimalization auto")
------------ | -------------

## Future plans

<p>There are 3 most important steps in front of MGP. First one is get used by as much open source ventilator projects as possible. This way the effort of devoted people can be used with more efficiency in the near future. After MGP proved its strength it’s time to make the next step forward.</p>
<p>Second step is to reach the use of MGP based solutions in the medical industry too. Open source projects are not real competitors for traditional companies of the healthcare industry but the experience with low cost hardware and the know-how of home made design can improve their manufacturing too. The situation is just the same with the software. Differences in the field of performance or quality of hardware parts happen in normal processes too when manufacturers should change their suppliers. MGP has a clearly separated workflow, and a very flexible structure. Behavior of the software can be changed even runtime. Therefore we are thinking in a changing world which we might face in the near future our solution is a good platform for healthcare industry to build ventilators.</p>
<p>If we proved the strength of Medical Gateway Platform in maintaining and remote controlling ventilators we are eager to step even forward and use MGP in case of other medical devices as well to build a strongly unified medical platform for a highly data driven use.</p>
<p>We are thinking with open source code companies can build cheap solutions quickly. This ability can help the companies in Europe to have greater share in the world scale medical industry. We aim to utilize those facts and circumstances to promote our solution for everyone.</p>

## Additional information

We are using ` requirements.txt ` and ` CHANGELOG.md `
