---
title: "The Canary in the Parking Lot: Why the Capacity to Remain Is the First Thing a Site Sheds"
author: "PIATRA . INSTITUTE"
date: "September 2026"
---

## Abstract

A drive-in restaurant can be criticised for its land and fuel use and regretted for the social uses lost when it closes. The two judgements concern different quantities: profitability, ecological cost and the uses a place supports. We model a site as a set of functions, each with a footprint, a social value and an appropriability, the share of its value the operator can charge for. Under rising ground rent an operator removes functions in order of private return per unit footprint. The five functions that let people remain on site are removed first, whereas an ordering by social value would first remove the parking the transaction requires. With uniform appropriability the two orders coincide. Seating disappears well before closure: the last way of staying is removed at a ground rent of 13.2 and the site closes at 81.9, and when the last seat goes the site still earns 0.588 of its peak profit while having lost 0.423 of its social value. Removing every way of staying reduces the ecological burden of a meal occasion by 0.0212, and by no more than 0.0377 across 1482 combinations of travel parameters, because most of the burden comes from travel the operator does not control. An obligation triggered by on-premises capacity can be avoided by removing that capacity: a duty worth 0.0704 of private return leads to the removal of 0.3226 of social value. A United States district court accepted an exemption on this basis in 1966, and it was reversed on appeal.

## Introduction

The drive-in restaurant is open to two criticisms that appear to conflict. It used large amounts of land and depended on car travel, and its disappearance also removed places where people could spend time without spending much money. The two judgements concern different quantities: commercial return, ecological cost, and the uses a site supports. We ask under what conditions competitive redesign removes the socially useful functions of a site while leaving its material dependencies unchanged, and we answer with an explicit model.

The central quantity is appropriability, the share of the value a function creates that its provider can capture. The concept comes from the economics of innovation, where returns depend on appropriability as well as on the value created [@teece1986]. For a restaurant, the transaction is almost fully appropriable, since the operator charges for it directly. A place to sit after paying has low appropriability, because most of its value goes to the people using it and to the people they meet.

In organisational economics, slack refers to resources held within a firm beyond what production requires, usually treated as a buffer against shocks or as evidence of agency costs [@cyert1963; @bourgeois1981]. The capacity studied here lies outside the firm and benefits users, so results from that literature do not carry over.

The model has ten functions whose footprints, social values and appropriabilities are stipulated and listed in full. Nothing is fitted to a real business and no company is named. The computations use exhaustive grids and a seeded ensemble, and a set of invariants is checked on every run. The historical case discussed later is documentary and was verified independently of the model, which is not calibrated to it.

## Related work

Ritzer described the rationalisation of fast food and its extension to digital ordering, in which customers take on work previously done by staff [@ritzer1983; @ritzer2018]; the model adds an account of which functions rationalisation removes first. Horkheimer's critique of procedures optimised without examination of their purpose [@horkheimer1947] applies to speed of service. The model does not settle that question, but it shows that the quantity being optimised and the quantity being lost are distinct. Lefebvre distinguished space as a measured parcel from space as it is lived [@lefebvre1991], and the two orderings computed below correspond to that distinction.

The rent mechanism follows Marx on building-site rent and Smith on the gap between the rent a site yields under its current use and under a potential one [@marx1894; @smith1979], within Harvey's account of the spatial organisation of capital [@harvey1982]. Smith developed the rent gap for gentrification, so its application to roadside businesses is an extension. Following Aalbers, we reserve the term financialisation for cases involving identifiable financial actors, instruments or valuation practices [@aalbers2016]; the mechanism modelled here is rent pressure.

Research on automobility treats car dependence as a system of mutually reinforcing arrangements [@shelleryurry2000; @urry2004; @gorz1973], which explains why redesigning a site leaves the travel to it unchanged. Fraser's account of social reproduction describes capacities on which accumulation depends and which it does not pay for [@fraser2016]. An afternoon at a restaurant table is not care work, but the structure is similar: a site can support relationships that its customers' individual purchases do not pay for, which is what low appropriability means in this setting.

Oldenburg's account of informal public places [@oldenburg1989] and Whyte's observations of small urban spaces [@whyte1980] describe what such places require, including accessibility, no obligation to spend, and somewhere to sit; the ten functions in the model are our itemisation of those requirements. Benjamin's practice of reading ordinary commercial documents for evidence of the social order that produced them [@benjamin1999] is applied to a court record below. Marx's distinction between what a thing does for people and the exchange through which access to it is bought [@marx1867] is an earlier and more general form of the distinction that appropriability measures.

## The model

Each function has a footprint in space and time, a social value, and an appropriability. Private return is appropriability multiplied by social value, so appropriability is the only substantive stipulation. Facing a ground rent, an operator keeps a function while its private return covers the rent on its footprint, which orders removals by private return per unit footprint. A public evaluation of the same site would order them by social value per unit footprint.

## Order of removal under rising ground rent

With the stipulated values, the operator removes functions in this order: meeting others without buying, staying after the purchase is finished, tables and chairs, restrooms open to customers, shelter from weather, parking long enough to be served, a wider menu than the minimum, collecting an order without parking, preparing the food, and ordering and payment. The five functions that let people stay are removed before any transactional function.

The social ordering differs from the private one without reversing it; the rank correlation between the two is 0.556. The main difference concerns parking. By social value per unit footprint, the first function to remove is the parking needed for the transaction, which occupies a large footprint for a modest value. The operator keeps it until sixth, three places after tables and chairs. Under rent pressure the site therefore keeps the parking that serves car access and loses the functions that let people stay, as a consequence of where appropriability is high and where it is low.

With appropriability set to the same value for every function, the two orders coincide and the rank correlation is exactly 1.000. The divergence is therefore caused entirely by differences in appropriability.

For each function, the ratio of social value to private return is the reciprocal of its appropriability and measures the social value lost per unit of private return forgone when the function is removed. The ratio is 25.0 for the first function removed and 1.053 for the last, so the functions removed earliest are those whose removal costs other people the most per unit of the operator's saving.

## Removal of seating before closure

Because the ways of staying are removed early and the transaction last, the two events are separated by a wide range of rent. The last way of staying disappears at a ground rent of 13.2. The site closes, in the sense that its earnings no longer cover the rent on what it occupies plus the fixed cost of operating, at a ground rent of 81.9, a ratio of 6.20. Measured from the removal of the first way of staying, the ratio is 61.4. The site stays open across 0.839 of the rent range while offering nowhere to stay.

When the last seat is removed, the site still earns 0.588 of its peak profit and has lost 0.423 of its social value, so its accounts show a profitable business. Closure is therefore a late indicator of rent pressure. The removal of seating is an earlier indicator, and it is not usually recorded.

![Order of removal and timing relative to closure. (a) The ground rent at which each function stops covering the rent on its footprint, on a logarithmic scale; the five ways of staying lie below the dashed line. (b) Social value provided, ways of staying provided, and profit relative to its peak, as ground rent rises; the shaded band is the range over which the site is open with nowhere to stay. (c) The operator's order of removal against the order implied by social value, with the rank correlation between them.](../simulation/output/figures/order.png)

## Ecological burden of a meal occasion

Consider a meal occasion at a site reached by car, with three sources of burden: travel, food and the site itself. The operator pays for the site, charges for the food, and neither pays for nor controls the travel. Under the stipulated values travel accounts for 2.28 and food for 2.50 of a total of 5.00 kg CO$_2$e, and the site for 0.22, or 0.044 of the total. Redesign affects only part of the site's share. Removing all five functions that let people stay reduces the total burden of a meal occasion by 0.0212.

To check that this result does not depend on one emission factor, the calculation was repeated for 1482 combinations of round-trip length from 2 to 30 kilometres and emissions from 0.05 to 0.30 kilograms per kilometre. The reduction never exceeds 0.0377 and never falls below 0.00906. The site's own burden would have to be 21.7 times the stipulated value for it to account for half the burden of a meal occasion.

The combination of lower social value and unchanged ecological burden is therefore the generic outcome for a site reached by car. An operator minimising the costs it bears removes the functions with the lowest private yield, which are the ways of staying, and leaves the travel unchanged because the travel is outside its control. The opposite outcome is possible: replacing a site with housing, a public square and services within walking distance would reduce travel and increase shared use, and the model allows it. Profit maximisation does not select it, because the change it requires is not one the operator can make.

## Obligations attached to on-premises capacity

Suppose an obligation applies to a site because it provides somewhere to stay, for example a duty of non-discrimination, accessibility, licensing or rates. If the duty scales with the capacity provided, it lowers the rent at which that capacity is removed by exactly its own rate; removing every way of staying at zero rent would require a duty rate of 13.2. If instead the duty applies only above a threshold, so that a site owes nothing once its capacity falls below some share, the duty creates a discontinuity.

With the threshold at a tenth of the site, an operator can fall below it by removing three functions: meeting others without buying, staying after the purchase is finished, and tables and chairs. The private return given up is 0.0704 of the site's total, so any duty costing more than that is avoided by removing them, at any ground rent including zero. The social value lost is 0.3226 of the site's total. The share of social value lost is 4.580 times the share of private return given up. Where the threshold is set so that removing one function suffices, this ratio equals that function's own social-to-private ratio: a duty worth 0.00555 of private return leads to the removal of the opportunity to meet others without buying, with a loss of 0.0806 of social value, a ratio of 25.0.

## The 1966 drive-in case

The mechanism has a documented instance. In 1966 a federal district court held that five drive-in restaurants in South Carolina were outside Title II of the Civil Rights Act of 1964. The statutory category was a facility "principally engaged in selling food for consumption on the premises," and the court found that the drive-ins had "no tables and chairs, or counters, bars or stools... sufficient to accommodate any appreciable number of patrons," that "the service is geared to service in the customers' cars," that "customers are encouraged to consume the food off the premises by its service in disposable containers," and that half of their food was eaten elsewhere. The one establishment in the group with tables and chairs, a downtown sandwich shop, was held to be covered, and the five drive-ins were not [@newman1966].

The findings also describe the discrimination at issue. The court found that discrimination at all six establishments was uncontested and completely established by the evidence, and that "the limited Negro customers who are served must place and pick up their orders at the kitchen windows and are not permitted to consume their purchases on the premises" [@newman1966]. Purchase and presence were separated in practice, and the statute turned on the same distinction.

The Court of Appeals reversed the refusal to enjoin discrimination at the drive-ins [@newman1967], and the Supreme Court, which heard the case on the separate question of attorney's fees, stated that the district court had "erroneously concluded that Title II does not cover drive-in restaurants of the sort involved in this case" [@newman1968]. The reasoning was rejected, but the incentive it reveals remains wherever an obligation depends on a threshold of on-premises capacity: the model predicts that the cheapest response is to reduce capacity below the threshold, and the court record shows that response being argued.

![Ecological burden and threshold obligations. (a) The burden of one meal occasion in stipulated units, divided into travel, food, and the site the operator controls. (b) The reduction in total burden from removing every way of staying, across trip lengths and emission factors. (c) The share of private return an operator gives up to avoid a threshold duty, and the share of social value lost, as the threshold varies.](../simulation/output/figures/burden.png)

## Robustness of the ordering

Because the ordering depends on stipulated numbers, it was tested with an ensemble in which every footprint and every appropriability was multiplied by an independent uniform factor between 0.6 and 1.4, 800 times.

The first function removed was a way of staying in 1.000 of the draws, that is, in all 800. All five ways of staying were among the first six removed in 0.971 of the draws, and in the least favourable draw their mean rank was 3.6 out of ten. The stronger statement that they are exactly the first five holds in 0.538 of the draws, so the precise ordering is sensitive to the parameters while the general pattern is not. The rank correlation between the private and social orders has a median of 0.467 and a maximum of 0.822, and never reaches the value of 1.000 produced by uniform appropriability.

## Historical and interpretive cautions

Arguments about lost social places tend to locate a better world just before the present, as Williams showed for English writing about the countryside [@williams1973]. The model is not tied to a period. It states that functions whose value goes mainly to people other than the operator are removed early under rent pressure, and that statement applies to any period.

Whether nostalgic representations obscure history or engage with it is contested. Jameson read nostalgia as a surface standing in for the past [@jameson1984], whereas Dika argued that some of the same films engage the conditions they depict [@dika2003]. We take no position. Memory is neither reliable evidence nor simply false consciousness, and it is the main testimony available about what these places were used for.

The court record gives a further reason for caution. At the six South Carolina establishments, some customers could buy food but could not stay. Any account of a lost shared space has to ask among whom it was shared, and the model cannot answer that question.

The sectoral history is also more complicated than a single decline. Roadside restaurants developed under the influence of highway construction, franchising and labour supply, and were being rationalised well before the period usually blamed [@jakle1999]. Drive-in cinemas had different economics and a different decline [@foxblack2011]. This study concerns restaurants and reports no counts for either.

Bataille argued against the requirement that every activity justify itself by what it produces [@bataille1988], which describes the kind of value the model assigns to time spent on site without purchasing. The argument does not extend to land and fuel: time spent without purchasing and the consumption of scarce materials are separate quantities, and the burden calculation treats them separately for that reason.

## Limitations

The ten functions and their parameters are stipulated. Appropriability is the central assumption, and no empirical estimate of it exists for any of these functions; the ensemble varies it but cannot validate it. The direction of the result follows from the difference between chargeable and unchargeable value, and the magnitudes depend on parameters that have not been measured. The ensemble perturbs parameter values and leaves the functional forms fixed.

The model says nothing about the people who provide the service. Service work has its own history and organisation [@cobble1992], and the model does not address whether the loss of a service role benefits or harms the workers concerned.

The model has no distributional content. It treats the capacity to stay as one quantity, although access to it has never been equal, as the 1966 case shows: at all six establishments purchase and presence were separated by race. The model cannot ask whose presence is at stake. The car had a similar double role, giving Black travellers real autonomy and protection under segregation while businesses it took them to refused them service [@sorin2020].

The results are not an argument for preserving particular sites. A former drive-in converted to housing, a public square and services within walking distance would reduce travel and increase shared use; the model allows that outcome, and profit maximisation does not select it. The results concern the capacity to stay, which a building, a car park or a vehicle may or may not provide.

The results do not show that capitalism cannot tolerate what it cannot charge for. If a function's appropriability is high enough, it survives any rent that the business survives, and firms that find sociability profitable provide it. The claim is narrower: functions whose value goes mainly to people other than the operator are removed first and well before the operator faces difficulty, removing them does not reduce the ecological burden, and obligations tied to them make removing them more attractive.

## References
