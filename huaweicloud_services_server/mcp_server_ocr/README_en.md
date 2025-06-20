# OCR MCP Server 


## Version
v0.1.0

## Overview

OCR MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service OCR. Full-chain management of OCR resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Accepted Bill Identification | RecognizeAcceptanceBill | Identifies key information in the acceptance bill and returns structured results in JSON format. | To be tested |
| Airplane itinerary identification | RecognizeFlightItinerary | Identifies text information in the aircraft itinerary and returns the structured recognition result. | To be tested |
| Bank Card OCR | RecognizeBankcard | Identifies key text information on bank cards and returns the structured recognition result. | To be tested |
| Bank Receipt Identification | RecognizeBankReceipt | Supports text recognition and key-value pair extraction for bank receipts, implementing efficient automatic and structured return. | To be tested |
| Business Card Recognition | RecognizeBusinessCard | Identifies the text information on the business card image and returns the structured recognition result. Extracts structured information from business cards in different formats. | To be tested |
| Business License Identification | RecognizeBusinessLicense | Identifies text information in the image on the business license home page and returns the structured recognition result.  | To be tested |
| Colombian Identity Card Identification | RecognizeColombiaIdCard | Identifies the text information in the Colombian ID card and returns the recognition result to the user. | To be tested |
| Customized template OCR | RecognizeCustomTemplate | Customized template OCR: Users can customize templates. For various bills and cards with fixed formats, users can specify key fields to be identified on the GUI to automatically identify and extract images in specific formats. | To be tested |
| Document Book Identification | RecognizeHouseholdRegister | Identifies text information in the household register and returns the structured recognition result.  | To be tested |
| Driver's license recognition | RecognizeDriverLicense | Identifies the driver's license image uploaded by the user. (or the URL of the driver's license image file on OBS on HUAWEI CLOUD provided by the user) The text content of the homepage and secondary page in the, and the recognition result is returned to the user. | To be tested |
| Electronic Sheet Identification | RecognizeWaybillElectronic | Identifies the text content in the electronic sheet image uploaded by the user and returns the recognition result in JSON format to the user. | To be tested |
| Financial Statement Identification | RecognizeFinancialStatement | Identifies the text in the table image uploaded by the user and returns the recognition result to the user. | To be tested |
| General OCR | RecognizeGeneralText | Recognizes the text information on the image and returns the recognized text and coordinates. Supports text recognition in multiple scenarios, such as scanning files, electronic documents, books, bills, and forms. | To be tested |
| General Table Identifier | RecognizeGeneralTable | Identifies a common table image uploaded by a user. (or URL of the general table image file on OBS on HUAWEI CLOUD provided by the user) Text content in and return the recognition result to the user.  | To be tested |
| Handwritten Character Recognition | RecognizeHandwriting | Identifies handwritten text information in a document and returns the recognition result to the user.  | To be tested |
| Identity Card Recognition | RecognizeIdCard | Identifies the text in the ID card image and returns the recognition result to the user.  | To be tested |
| Insurance policy identification | RecognizeInsurancePolicy | Identifies the text information on the insurance policy image and returns the recognition result to the user. Structured information can be extracted from scanned images and mobile phone photos of insurance policies in multiple formats.  | To be tested |
| Intelligent classification recognition | RecognizeAutoClassification | Detects the ticket (ticket, certificate, or other text carrier) specified on the location image to be recognized and performs structured recognition on the ticket. The interface returns the location coordinates of the ticket to be recognized on the image, the content to be recognized in a structured manner, and the corresponding category in a list. | To be tested |
| Invoice verity | RecognizeInvoiceVerification | The invoice verification service supports the information verification of 10 types of VAT invoices, including VAT special invoices, VAT ordinary invoices, VAT ordinary invoices (roll-type), VAT electronic special invoices, VAT electronic ordinary invoices, and VAT electronic ordinary invoices (toll)), unified invoice for used car sales, unified invoice for motor vehicle sales, electronic invoice for blockchain, and all-electric invoice. All information about the ticket face can be returned.  | To be tested |
| License plate recognition | RecognizeLicensePlate | Identifies the license plate information in the input image and returns the coordinates and content of the license plate information. | To be tested |
| Motor Vehicle Sales Invoice Recognition | RecognizeMvsInvoice | Recognize motor vehicle sales invoices and used vehicle sales invoices. (The service can automatically distinguish the two types and return the corresponding fields.) Text content in and the recognition result is returned to the user in JSON format. | To be tested |
| Network Image OCR | RecognizeWebImage | Identifies text in network images and returns the structured recognition result. | To be tested |
| Passport ID | RecognizePassport | Identifies the text information in the passport home page image uploaded by the user and returns the structured recognition result. In the current version, all fields of Chinese passports can be identified. Foreign passports support the identification of the two internationally standardized machine-readable codes below the passport, and can extract 6-7 key fields from them.  | To be tested |
| Quota Invoice Identification | RecognizeQuotaInvoice | Identifies text information in quota invoices and returns the recognition result.  | To be tested |
| Real Property Certificate Identification | RecognizeRealEstateCertificate | Identifies the text information in the real estate certificate and returns the structured recognition result.  | To be tested |
| Road Transport License Identification | RecognizeTransportationLicense | Identifies the text information on the first page of the road transport license and returns the structured recognition result.  | To be tested |
| Road Transport Qualification Certificate Identification | RecognizeQualificationCertificate | Identifies the key text information on the road transport qualification certificate and returns the structured recognition result.  | To be tested |
| Seal Identification | RecognizeSeal | Detects and identifies seals in contract files or common bills, erases and extracts seals from images, and returns the results of seal detection, identification, erasing, and extraction in JSON format. | To be tested |
| Smart Document Parsing | RecognizeSmartDocumentRecognizer | Extracts key-value pairs, recognizes characters, and recognizes tables for documents in any format, such as certificates, receipts, and forms, implementing advanced and efficient automatic and structured return.  | To be tested |
| Taxi Invoice OCR | RecognizeTaxiInvoice | Identifies text information in taxi invoices and returns the structured recognition result.  | To be tested |
| Thai Identity Card Recognition | RecognizeThailandIdcard | Identifies the text information in the Thai ID card and returns the structured recognition result. | To be tested |
| Thailand License Plate Recognition | RecognizeThailandLicensePlate | Identifies the license plate information in the Thailand license plate image and returns the structured recognition result. | To be tested |
| Train ticket recognition | RecognizeTrainTicket | Identifies text information in train tickets and returns the structured recognition result.  | To be tested |
| VAT Invoice Recognition | RecognizeVatInvoice | Identifies the type of the VAT invoice and the text content in the image, and returns the recognition result in JSON format. Authenticity verification is not supported.  | To be tested |
| VIN code identification | RecognizeVin | Recognize the vehicle frame number in the image and return the recognition result to the user.  | To be tested |
| Vehicle Certificate Identification | RecognizeVehicleCertificate | Identifies text information in the vehicle certificate and returns the structured recognition result.  | To be tested |
| Vehicle Toll Invoice OCR | RecognizeTollInvoice | Identifies text information in a vehicle toll invoice and returns the recognition result.  | To be tested |
| Vicient license recognition | RecognizeVehicleLicense | Identifies the vehicle license image uploaded by the user. (or the URL of the vehicle license image file on OBS on HUAWEI CLOUD provided by the user) The text content of the homepage and secondary page in the, and the recognition result is returned to the user. | To be tested |

