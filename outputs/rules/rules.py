def findDecision(obj): #obj[0]: Gender, obj[1]: Married, obj[2]: Dependents, obj[3]: Education, obj[4]: Self_Employed, obj[5]: ApplicantIncome, obj[6]: CoapplicantIncome, obj[7]: LoanAmount, obj[8]: Loan_Amount_Term, obj[9]: Credit_History, obj[10]: Property_Area
	# {"feature": "Credit_History", "instances": 614, "metric_value": 0.8963, "depth": 1}
	if obj[9]>0.0:
		# {"feature": "ApplicantIncome", "instances": 475, "metric_value": 0.7303, "depth": 2}
		if obj[5]>150:
			# {"feature": "CoapplicantIncome", "instances": 474, "metric_value": 0.727, "depth": 3}
			if obj[6]<=9173.771886754848:
				# {"feature": "Loan_Amount_Term", "instances": 470, "metric_value": 0.7177, "depth": 4}
				if obj[8]<=360.0:
					# {"feature": "Self_Employed", "instances": 460, "metric_value": 0.7042, "depth": 5}
					if obj[4] == 'No':
						# {"feature": "LoanAmount", "instances": 373, "metric_value": 0.7133, "depth": 6}
						if obj[7]<=299.5760476586453:
							# {"feature": "Gender", "instances": 358, "metric_value": 0.6895, "depth": 7}
							if obj[0] == 'Male':
								# {"feature": "Education", "instances": 291, "metric_value": 0.654, "depth": 8}
								if obj[3] == 'Graduate':
									# {"feature": "Dependents", "instances": 226, "metric_value": 0.5998, "depth": 9}
									if obj[2] == '0':
										# {"feature": "Married", "instances": 129, "metric_value": 0.6223, "depth": 10}
										if obj[1] == 'Yes':
											# {"feature": "Property_Area", "instances": 79, "metric_value": 0.548, "depth": 11}
											if obj[10] == 'Semiurban':
												return 'Y'
											elif obj[10] == 'Rural':
												return 'Y'
											elif obj[10] == 'Urban':
												return 'Y'
											else: return 'Y'
										elif obj[1] == 'No':
											# {"feature": "Property_Area", "instances": 50, "metric_value": 0.7219, "depth": 11}
											if obj[10] == 'Urban':
												return 'Y'
											elif obj[10] == 'Semiurban':
												return 'Y'
											elif obj[10] == 'Rural':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									elif obj[2] == '2':
										# {"feature": "Property_Area", "instances": 45, "metric_value": 0.4328, "depth": 10}
										if obj[10] == 'Urban':
											# {"feature": "Married", "instances": 19, "metric_value": 0.6292, "depth": 11}
											if obj[1] == 'Yes':
												return 'Y'
											else: return 'Y'
										elif obj[10] == 'Semiurban':
											return 'Y'
										elif obj[10] == 'Rural':
											# {"feature": "Married", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[1] == 'Yes':
												return 'Y'
											elif obj[1] == 'No':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									elif obj[2] == '1':
										# {"feature": "Married", "instances": 31, "metric_value": 0.7088, "depth": 10}
										if obj[1] == 'Yes':
											# {"feature": "Property_Area", "instances": 29, "metric_value": 0.7355, "depth": 11}
											if obj[10] == 'Urban':
												return 'Y'
											elif obj[10] == 'Semiurban':
												return 'Y'
											elif obj[10] == 'Rural':
												return 'Y'
											else: return 'Y'
										elif obj[1] == 'No':
											return 'Y'
										else: return 'Y'
									elif obj[2] == '3+':
										# {"feature": "Property_Area", "instances": 17, "metric_value": 0.6723, "depth": 10}
										if obj[10] == 'Rural':
											return 'Y'
										elif obj[10] == 'Urban':
											# {"feature": "Married", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[1] == 'Yes':
												return 'Y'
											else: return 'Y'
										elif obj[10] == 'Semiurban':
											# {"feature": "Married", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[1] == 'Yes':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									else: return 'Y'
								elif obj[3] == 'Not Graduate':
									# {"feature": "Property_Area", "instances": 65, "metric_value": 0.8051, "depth": 9}
									if obj[10] == 'Rural':
										# {"feature": "Dependents", "instances": 24, "metric_value": 0.9544, "depth": 10}
										if obj[2] == '0':
											# {"feature": "Married", "instances": 14, "metric_value": 0.9403, "depth": 11}
											if obj[1] == 'No':
												return 'Y'
											elif obj[1] == 'Yes':
												return 'Y'
											else: return 'Y'
										elif obj[2] == '2':
											# {"feature": "Married", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[1] == 'Yes':
												return 'Y'
											else: return 'Y'
										elif obj[2] == '3+':
											# {"feature": "Married", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1] == 'Yes':
												return 'N'
											else: return 'N'
										elif obj[2] == '1':
											return 'Y'
										else: return 'Y'
									elif obj[10] == 'Semiurban':
										# {"feature": "Married", "instances": 21, "metric_value": 0.2762, "depth": 10}
										if obj[1] == 'Yes':
											return 'Y'
										elif obj[1] == 'No':
											# {"feature": "Dependents", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[2] == '0':
												return 'Y'
											elif obj[2] == '3+':
												return 'Y'
											elif obj[2] == '1':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									elif obj[10] == 'Urban':
										# {"feature": "Dependents", "instances": 20, "metric_value": 0.8813, "depth": 10}
										if obj[2] == '0':
											# {"feature": "Married", "instances": 8, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Yes':
												return 'Y'
											elif obj[1] == 'No':
												return 'N'
											else: return 'N'
										elif obj[2] == '1':
											# {"feature": "Married", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[1] == 'Yes':
												return 'Y'
											else: return 'Y'
										elif obj[2] == '2':
											return 'Y'
										elif obj[2] == '3+':
											return 'N'
										else: return 'N'
									else: return 'Y'
								else: return 'Y'
							elif obj[0] == 'Female':
								# {"feature": "Dependents", "instances": 63, "metric_value": 0.7919, "depth": 8}
								if obj[2] == '0':
									# {"feature": "Property_Area", "instances": 47, "metric_value": 0.7046, "depth": 9}
									if obj[10] == 'Semiurban':
										# {"feature": "Married", "instances": 24, "metric_value": 0.4138, "depth": 10}
										if obj[1] == 'No':
											# {"feature": "Education", "instances": 15, "metric_value": 0.5665, "depth": 11}
											if obj[3] == 'Graduate':
												return 'Y'
											elif obj[3] == 'Not Graduate':
												return 'Y'
											else: return 'Y'
										elif obj[1] == 'Yes':
											return 'Y'
										else: return 'Y'
									elif obj[10] == 'Rural':
										# {"feature": "Married", "instances": 12, "metric_value": 0.9799, "depth": 10}
										if obj[1] == 'No':
											# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 11}
											if obj[3] == 'Graduate':
												return 'Y'
											elif obj[3] == 'Not Graduate':
												return 'Y'
											else: return 'Y'
										elif obj[1] == 'Yes':
											return 'N'
										else: return 'N'
									elif obj[10] == 'Urban':
										# {"feature": "Married", "instances": 11, "metric_value": 0.684, "depth": 10}
										if obj[1] == 'No':
											# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 11}
											if obj[3] == 'Graduate':
												return 'Y'
											elif obj[3] == 'Not Graduate':
												return 'Y'
											else: return 'Y'
										elif obj[1] == 'Yes':
											return 'N'
										else: return 'N'
									else: return 'Y'
								elif obj[2] == '1':
									# {"feature": "Married", "instances": 10, "metric_value": 0.971, "depth": 9}
									if obj[1] == 'No':
										# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[3] == 'Graduate':
											# {"feature": "Property_Area", "instances": 6, "metric_value": 1.0, "depth": 11}
											if obj[10] == 'Urban':
												return 'Y'
											elif obj[10] == 'Semiurban':
												return 'N'
											elif obj[10] == 'Rural':
												return 'Y'
											else: return 'Y'
										elif obj[3] == 'Not Graduate':
											return 'N'
										else: return 'N'
									elif obj[1] == 'Yes':
										return 'Y'
									else: return 'Y'
								elif obj[2] == '2':
									# {"feature": "Married", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1] == 'Yes':
										# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3] == 'Graduate':
											# {"feature": "Property_Area", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10] == 'Urban':
												return 'N'
											else: return 'N'
										else: return 'N'
									elif obj[1] == 'No':
										return 'N'
									else: return 'N'
								elif obj[2] == '3+':
									return 'Y'
								else: return 'Y'
							else: return 'Y'
						elif obj[7]>299.5760476586453:
							# {"feature": "Married", "instances": 15, "metric_value": 0.9968, "depth": 7}
							if obj[1] == 'Yes':
								# {"feature": "Gender", "instances": 11, "metric_value": 0.8454, "depth": 8}
								if obj[0] == 'Male':
									# {"feature": "Property_Area", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[10] == 'Urban':
										# {"feature": "Dependents", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[2] == '1':
											# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == 'Graduate':
												return 'Y'
											else: return 'Y'
										elif obj[2] == '0':
											return 'Y'
										else: return 'Y'
									elif obj[10] == 'Rural':
										# {"feature": "Dependents", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2] == '0':
											return 'N'
										elif obj[2] == '3+':
											return 'Y'
										else: return 'Y'
									elif obj[10] == 'Semiurban':
										return 'Y'
									else: return 'Y'
								elif obj[0] == 'Female':
									return 'Y'
								else: return 'Y'
							elif obj[1] == 'No':
								return 'N'
							else: return 'N'
						else: return 'Y'
					elif obj[4] == 'Yes':
						# {"feature": "LoanAmount", "instances": 62, "metric_value": 0.7088, "depth": 6}
						if obj[7]<=262.26737185487383:
							# {"feature": "Dependents", "instances": 56, "metric_value": 0.7496, "depth": 7}
							if obj[2] == '0':
								# {"feature": "Married", "instances": 28, "metric_value": 0.6769, "depth": 8}
								if obj[1] == 'No':
									# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 9}
									if obj[3] == 'Graduate':
										# {"feature": "Gender", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[0] == 'Male':
											# {"feature": "Property_Area", "instances": 8, "metric_value": 0.8113, "depth": 11}
											if obj[10] == 'Semiurban':
												return 'Y'
											elif obj[10] == 'Urban':
												return 'N'
											elif obj[10] == 'Rural':
												return 'Y'
											else: return 'Y'
										elif obj[0] == 'Female':
											# {"feature": "Property_Area", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10] == 'Semiurban':
												return 'N'
											elif obj[10] == 'Rural':
												return 'N'
											else: return 'N'
										else: return 'N'
									elif obj[3] == 'Not Graduate':
										return 'Y'
									else: return 'Y'
								elif obj[1] == 'Yes':
									# {"feature": "Education", "instances": 13, "metric_value": 0.3912, "depth": 9}
									if obj[3] == 'Graduate':
										return 'Y'
									elif obj[3] == 'Not Graduate':
										# {"feature": "Property_Area", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[10] == 'Urban':
											return 'Y'
										elif obj[10] == 'Semiurban':
											return 'N'
										elif obj[10] == 'Rural':
											return 'Y'
										else: return 'Y'
									else: return 'Y'
								else: return 'Y'
							elif obj[2] == '1':
								# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 8}
								if obj[3] == 'Graduate':
									# {"feature": "Property_Area", "instances": 12, "metric_value": 0.8113, "depth": 9}
									if obj[10] == 'Semiurban':
										return 'Y'
									elif obj[10] == 'Rural':
										# {"feature": "Married", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Yes':
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[0] == 'Male':
												return 'N'
											else: return 'N'
										elif obj[1] == 'No':
											return 'N'
										else: return 'N'
									elif obj[10] == 'Urban':
										# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0] == 'Male':
											# {"feature": "Married", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Yes':
												return 'N'
											else: return 'N'
										else: return 'N'
									else: return 'Y'
								elif obj[3] == 'Not Graduate':
									return 'N'
								else: return 'N'
							elif obj[2] == '2':
								# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[3] == 'Graduate':
									# {"feature": "Property_Area", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[10] == 'Rural':
										return 'Y'
									elif obj[10] == 'Semiurban':
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0] == 'Male':
											# {"feature": "Married", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1] == 'Yes':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									elif obj[10] == 'Urban':
										return 'Y'
									else: return 'Y'
								elif obj[3] == 'Not Graduate':
									# {"feature": "Property_Area", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[10] == 'Semiurban':
										return 'Y'
									elif obj[10] == 'Rural':
										return 'N'
									else: return 'N'
								else: return 'Y'
							elif obj[2] == '3+':
								return 'Y'
							else: return 'Y'
						elif obj[7]>262.26737185487383:
							return 'Y'
						else: return 'Y'
					else: return 'Y'
				elif obj[8]>360.0:
					# {"feature": "Married", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'No':
						# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0] == 'Male':
							return 'N'
						elif obj[0] == 'Female':
							# {"feature": "LoanAmount", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]>113.0:
								return 'N'
							elif obj[7]<=113.0:
								return 'Y'
							else: return 'Y'
						else: return 'N'
					elif obj[1] == 'Yes':
						# {"feature": "LoanAmount", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[7]<=123.0:
							return 'Y'
						elif obj[7]>123.0:
							return 'N'
						else: return 'N'
					else: return 'Y'
				else: return 'N'
			elif obj[6]>9173.771886754848:
				# {"feature": "Married", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1] == 'Yes':
					return 'N'
				elif obj[1] == 'No':
					# {"feature": "LoanAmount", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[7]>90.0:
						return 'Y'
					elif obj[7]<=90.0:
						return 'N'
					else: return 'N'
				else: return 'Y'
			else: return 'N'
		elif obj[5]<=150:
			return 'N'
		else: return 'N'
	elif obj[9]<=0.0:
		# {"feature": "LoanAmount", "instances": 139, "metric_value": 0.9006, "depth": 2}
		if obj[7]>51.147432296757046:
			# {"feature": "Loan_Amount_Term", "instances": 133, "metric_value": 0.9158, "depth": 3}
			if obj[8]>11.0:
				# {"feature": "CoapplicantIncome", "instances": 127, "metric_value": 0.9309, "depth": 4}
				if obj[6]<=10200.992370503067:
					# {"feature": "ApplicantIncome", "instances": 125, "metric_value": 0.9358, "depth": 5}
					if obj[5]>1025:
						# {"feature": "Self_Employed", "instances": 124, "metric_value": 0.9312, "depth": 6}
						if obj[4] == 'No':
							# {"feature": "Gender", "instances": 101, "metric_value": 0.9397, "depth": 7}
							if obj[0] == 'Male':
								# {"feature": "Married", "instances": 78, "metric_value": 0.9306, "depth": 8}
								if obj[1] == 'Yes':
									# {"feature": "Dependents", "instances": 59, "metric_value": 0.9647, "depth": 9}
									if obj[2] == '0':
										# {"feature": "Education", "instances": 26, "metric_value": 0.9957, "depth": 10}
										if obj[3] == 'Graduate':
											# {"feature": "Property_Area", "instances": 18, "metric_value": 0.9641, "depth": 11}
											if obj[10] == 'Urban':
												return 'Y'
											elif obj[10] == 'Rural':
												return 'N'
											elif obj[10] == 'Semiurban':
												return 'Y'
											else: return 'Y'
										elif obj[3] == 'Not Graduate':
											# {"feature": "Property_Area", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[10] == 'Urban':
												return 'N'
											elif obj[10] == 'Semiurban':
												return 'N'
											elif obj[10] == 'Rural':
												return 'N'
											else: return 'N'
										else: return 'N'
									elif obj[2] == '1':
										# {"feature": "Property_Area", "instances": 12, "metric_value": 0.9799, "depth": 10}
										if obj[10] == 'Rural':
											# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[3] == 'Graduate':
												return 'N'
											elif obj[3] == 'Not Graduate':
												return 'N'
											else: return 'N'
										elif obj[10] == 'Urban':
											# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[3] == 'Graduate':
												return 'Y'
											elif obj[3] == 'Not Graduate':
												return 'Y'
											else: return 'Y'
										elif obj[10] == 'Semiurban':
											# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == 'Graduate':
												return 'N'
											elif obj[3] == 'Not Graduate':
												return 'Y'
											else: return 'Y'
										else: return 'N'
									elif obj[2] == '3+':
										# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 10}
										if obj[3] == 'Graduate':
											# {"feature": "Property_Area", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[10] == 'Semiurban':
												return 'N'
											elif obj[10] == 'Rural':
												return 'N'
											elif obj[10] == 'Urban':
												return 'Y'
											else: return 'Y'
										elif obj[3] == 'Not Graduate':
											return 'N'
										else: return 'N'
									elif obj[2] == '2':
										# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[3] == 'Graduate':
											# {"feature": "Property_Area", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[10] == 'Urban':
												return 'N'
											elif obj[10] == 'Semiurban':
												return 'N'
											elif obj[10] == 'Rural':
												return 'N'
											else: return 'N'
										elif obj[3] == 'Not Graduate':
											# {"feature": "Property_Area", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[10] == 'Rural':
												return 'Y'
											elif obj[10] == 'Semiurban':
												return 'Y'
											elif obj[10] == 'Urban':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									else: return 'N'
								elif obj[1] == 'No':
									# {"feature": "Education", "instances": 19, "metric_value": 0.7425, "depth": 9}
									if obj[3] == 'Graduate':
										# {"feature": "Dependents", "instances": 14, "metric_value": 0.5917, "depth": 10}
										if obj[2] == '0':
											# {"feature": "Property_Area", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[10] == 'Rural':
												return 'N'
											elif obj[10] == 'Semiurban':
												return 'N'
											else: return 'N'
										elif obj[2] == '2':
											# {"feature": "Property_Area", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10] == 'Rural':
												return 'N'
											elif obj[10] == 'Semiurban':
												return 'Y'
											else: return 'Y'
										elif obj[2] == '1':
											return 'N'
										else: return 'N'
									elif obj[3] == 'Not Graduate':
										# {"feature": "Dependents", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[2] == '0':
											# {"feature": "Property_Area", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[10] == 'Urban':
												return 'N'
											elif obj[10] == 'Rural':
												return 'N'
											elif obj[10] == 'Semiurban':
												return 'Y'
											else: return 'Y'
										elif obj[2] == '1':
											return 'Y'
										else: return 'Y'
									else: return 'N'
								else: return 'N'
							elif obj[0] == 'Female':
								# {"feature": "Dependents", "instances": 20, "metric_value": 0.9928, "depth": 8}
								if obj[2] == '0':
									# {"feature": "Property_Area", "instances": 17, "metric_value": 0.9774, "depth": 9}
									if obj[10] == 'Semiurban':
										# {"feature": "Married", "instances": 9, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'No':
											# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[3] == 'Graduate':
												return 'N'
											else: return 'N'
										elif obj[1] == 'Yes':
											# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == 'Not Graduate':
												return 'N'
											elif obj[3] == 'Graduate':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									elif obj[10] == 'Urban':
										# {"feature": "Married", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[1] == 'No':
											# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[3] == 'Graduate':
												return 'N'
											else: return 'N'
										elif obj[1] == 'Yes':
											return 'N'
										else: return 'N'
									elif obj[10] == 'Rural':
										return 'Y'
									else: return 'Y'
								elif obj[2] == '2':
									return 'Y'
								elif obj[2] == '1':
									return 'Y'
								else: return 'Y'
							else: return 'N'
						elif obj[4] == 'Yes':
							# {"feature": "Dependents", "instances": 18, "metric_value": 0.9183, "depth": 7}
							if obj[2] == '0':
								# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[3] == 'Graduate':
									# {"feature": "Gender", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[0] == 'Female':
										# {"feature": "Property_Area", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[10] == 'Urban':
											return 'Y'
										elif obj[10] == 'Rural':
											return 'N'
										elif obj[10] == 'Semiurban':
											return 'N'
										else: return 'N'
									elif obj[0] == 'Male':
										# {"feature": "Married", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'No':
											# {"feature": "Property_Area", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10] == 'Urban':
												return 'N'
											else: return 'N'
										else: return 'N'
									else: return 'N'
								elif obj[3] == 'Not Graduate':
									return 'N'
								else: return 'N'
							elif obj[2] == '1':
								return 'N'
							elif obj[2] == '2':
								# {"feature": "Property_Area", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[10] == 'Rural':
									return 'Y'
								elif obj[10] == 'Semiurban':
									return 'N'
								else: return 'N'
							elif obj[2] == '3+':
								return 'Y'
							else: return 'Y'
						else: return 'N'
					elif obj[5]<=1025:
						return 'Y'
					else: return 'Y'
				elif obj[6]>10200.992370503067:
					return 'N'
				else: return 'N'
			elif obj[8]<=11.0:
				return 'N'
			else: return 'N'
		elif obj[7]<=51.147432296757046:
			return 'N'
		else: return 'N'
	else: return 'N'
